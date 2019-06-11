import numpy as np
from food import Food

class Environement(object):
	"""The class Environement where the blob are evolving"""
	def __init__(self, h, w, *args):
		self.h = h
		self.w = w
		self.food_board = np.empty((h,w), dtype=Food)
		self.blobs = list(args)

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

	


