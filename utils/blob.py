from random import random
import numpy as np
from math import sqrt

class Blob(object):
	"""Blob is the creature that is evolving in this simulation"""
	def __init__(self, x, y, speed, size, energy, sense, name='000'):
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
		self.can_clone = False
		self.is_moving = True
		self.nothing_todo = False

		self.name = name
		self.heritage = {'speed':speed,'size':size,'energy':energy,'sense':sense}

	def move(self, map):
		if self.energy >= self.energy_cost():
			if self.food < 2:
				if self.sense_food(map):
					food_positions = list(filter(self.caneat_food,map.get_foods_positions(self)))
					food_position = self.choice(food_positions)

					self.decrease_energy(self.energy_cost())
					self.eat_food(map,food_position)
				else:
					self.discover(map)	
			else:
				self.go_home(map)
		else:
			self.is_moving = False
			self.nothing_todo = True

	def go_home(self, map):
		distance_home = min([
			self.distance((0,self.y)),
			self.distance((map.h,self.y)),
			self.distance((self.x,0)),
			self.distance((0,map.w))
		])
		if self.cango_home(distance_home):
			self.safe = True
			self.x = 0
			if self.food >= 2: self.can_clone = True
			self.is_moving = False
			self.nothing_todo = True
		else:
			self.dead = True

	def discover(self, map):
		for s in range(self.speed):
			if self.energy > self.energy_cost():
				direction = np.random.randint(8)
				self.move_in_direction(direction, map)
				self.decrease_energy(self.energy_cost())
				self.move(map)

	def move_in_direction(self, direction, map):
		if direction == 0:
			self.x += 1
		elif direction == 1:
			self.x -= 1
		elif direction == 2:
			self.y -= 1
		elif direction == 3:
			self.y += 1
		elif direction == 4:
			self.x -= 1
			self.y -= 1
		elif direction == 5:
			self.x -= 1
			self.y += 1
		elif direction == 6:
			self.x += 1
			self.y -= 1
		elif direction == 7:
			self.x += 1
			self.y += 1

		if self.x < 0 : self.x = 0
		if self.x >= map.h : self.x = map.h - 1
		if self.y < 0 : self.y = 0
		if self.y >= map.w : self.y = map.w - 1

	def cango_home(self, distance):
		while self.energy >= 0 and distance > 0:
			distance -= 1
			self.decrease_energy(self.energy_cost())
		if distance <= 0:
			return True
		else:
			return False

	def go_to(self, position):
		self.x = position[0]
		self.y = position[1]

	def eat_food(self, map, position):
		self.food += 1
		self.x = position[0]
		self.y = position[1]
		map.remove_food(position[0],position[1])

	def caneat_food(self, p):
		return self.senseable(p[0],p[1])

	def senseable(self, x, y):
		max_x = self.x + self.sense
		min_x = self.x - self.sense

		max_y = self.y + self.sense
		min_y = self.y - self.sense

		if x in range(min_x,max_x+1) and y in range(min_y,max_y+1):
			return True
		return False

	def decrease_energy(self, energy_cost):
		self.energy -= energy_cost
	
	def clone(self):
		if self.food < 2:
			return None

		speed = self.speed
		if random() < self.eps_mutation:
			speed = self.mutation(self.speed)

		size = self.size
		if random() < self.eps_mutation:
			size = self.mutation(self.size)

		sense = self.sense
		if random() < self.eps_mutation:
			sense = self.mutation(self.sense)

		return Blob(self.x, self.y, speed, size, self.heritage['energy'], sense, name=self.name+' son')

	def is_possible(self, p):
		distance = self.distance(p)
		if distance <= self.move_formula():
			return True
		else:
			return False

	def sense_food(self, map):
		max_x = self.x + self.sense
		min_x = self.x - self.sense

		max_y = self.y + self.sense
		min_y = self.y - self.sense
		
		for x in range(min_x,max_x+1):
			for y in range(min_y, max_y+1):
				if (x > 0 and x < 10) and (y > 0 and y < 10): 
					if map.food_board[x,y] != None:
						return True

		return False

	def sense_positions(self,map):
		max_x = self.x + self.sense
		min_x = self.x - self.sense

		max_y = self.y + self.sense
		min_y = self.y - self.sense

		return [ (x, y) for x in range(min_x,max_x+1) for y in range(min_y, max_y+1) if x >= 0 and y >= 0]

	@staticmethod
	def mutation(trait):
		new_trait = trait
		if random() > 0.5:
			new_trait += np.random.randint(trait)
		else:
			new_trait -= np.random.randint(trait)
		return new_trait

	distance = lambda self, p: sqrt((self.x - p[0])**2+(self.y - p[1])**2) 

	energy_cost = lambda self: 2 * self.speed + self.size**2 + self.sense
	
	def reset(self):
		self.energy = self.heritage['energy']
		self.speed = self.heritage['speed']
		self.sense = self.heritage['sense']
		self.size = self.heritage['size']
		self.food = 0
		self.is_moving = True
		self.safe = True
		self.dead = False

	@staticmethod
	def choice(tuple_list):
		index = np.random.randint(0,len(tuple_list))
		return tuple_list[index]

	def __str__(self):
		return f'blob{self.name} : {self.food}{(self.x, self.y)}, speed {self.speed}, energy {self.energy}, size {self.size}'
