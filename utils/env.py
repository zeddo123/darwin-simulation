import numpy as np
from food import Food

class Environement(object):
	"""The Environement class where the blob are evolving"""
	def __init__(self, h, w, *args):
		self.turn_status = 0 # 0 for inactive 1 for active
		self.h = h
		self.w = w
		self.food_board = np.empty((h,w), dtype=Food) # matrixs where the food is
		self.blobs = list(args) # stores the living blobs

	def set_food(self):
		for r in range(self.h*self.w/3):
			x = np.random.randint(self.h)
			y = np.random.randint(self.w)
			self.food_board[x,y] = Food()

	def remove_food(self, x, y):
		if x in range(self.h) and y in range(self.w):
			self.food_board[x,y] = None

	def add_blob(self, blob):
		self.blobs = [blob] + self.blobs

	def remove_blob(self, blob):
		self.blobs.remove(blob)

	def get_foods_positions(self, blob):
		food = [(i, j) for i in range(self.h) for j in range(self.h) if self.food_board[i,j] != None]
		blob = [(b.x, b.y) for b in self.blobs if blob.size > b.size]
		return food + blob

	def get_positions(self, x, y):
		return [(i, j) for i in range(self.h) for j in range(self.h) if i != x and j != y]

	def simulate(self, generation=1):
		for g in range(generation):
			for blob in self.blobs:
				while not blob.safe or blob.dead:
					




