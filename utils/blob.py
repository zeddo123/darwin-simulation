from random import random

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

	def find_food(self, map):
		pass

	def reproduce(self):
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
	
	@staticmethod
	def mutation(trait):
		new_trait = trait
		if random() > 0.5:
			new_trait += random()
		else:
			new_trait -= random()