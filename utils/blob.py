from random import random
import numpy as np
from math import sqrt

class Blob(object):
	"""Blob is the creature that is evolving in this simulation"""
	def __init__(self, x, y, speed, size, energy, sense):
		self.speed = speed
		self.size = size
		self.energy = energy
		self.sense = sense

		self.food = 0
		self.eps_mutation = 0.3
		self.x = x
		self.y = y
		self.safe = False
		self.dead = False

	def move(self, map):
		if self.food < 2:
			if self.sense_food():
				food_position = np.random.choice(filter(caneat_food,map.get_foods_position(self)))
				self.decrease_energy(self.distance(food_position))
				self.eat_food(map,food_position)
			else:
				position = np.random.choice(filter(self.is_possible,map.get_position(self.x,self.y)))
				self.decrease_energy(self.distance(position))
		else:
			self.go_home(map)

	def go_home(self, map):
		# wrong solution (need fix)
		distance_top = self.is_possible(0,self.y) 
		distance_buttom = self.is_possible(map.h,self.y)
		distance_left = self.is_possible(self.x,0)
		distance_right = self.is_possible(0,map.w)
		if distance_top or distance_buttom or distance_left or distance_right:
			self.safe = True
		else:
			self.dead = True 

	def eat_food(self, map, position):
		self.food += 1
		map.remove_food(position[0],position[1])

	caneat_food = lambda p: self.is_possible(p[0],p[1]) and self.senseable(p[0],p[1])

	def senseable(self, x, y):
		max_x = self.x + self.sense
		min_x = self.x - self.sense

		max_y = self.y + self.sense
		min_y = self.y - self.sense

		if x in range(min_x,max_x+1) and y in range(min_y,max_y+1):
			return True
		return False

	def decrease_energy(self, distance):
		self.energy -= distance
	
	def clone(self):
		if food < 2:
			return None

		if random() < self.eps_mutation:
			speed = self.mutation(self.speed)

		if random() < self.eps_mutation:
			energy = self.mutation(self.energy)

		if random() < self.eps_mutation:
			size = self.mutation(self.size)

		if random() < self.eps_mutation:
			sense = self.mutation(self.sense)

		return Blob(self.x, self.y, speed, size, energy)

	def is_possible(self, x, y):
		distance = self.distance((x,y))
		if distance <= self.move_formula():
			return True
		else:
			return False

	@staticmethod
	def mutation(trait):
		new_trait = trait
		if random() > 0.5:
			new_trait += random()
		else:
			new_trait -= random()

	distance = lambda self, p: sqrt((self.x - p[0])**2+(self.y - p[1])**2) 

	move_formula = lambda self: (self.energy + self.speed)/self.size if self.energy != 0 else 0
