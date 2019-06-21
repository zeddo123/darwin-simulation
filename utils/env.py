from math import ceil
import numpy as np
from .food import Food

class Environement(object):
	"""The Environement class where the blob are evolving"""
	def __init__(self, h, w, *args):
		self.h = h # dementions of the environement
		self.w = w #
		self.food_board = np.empty((h,w), dtype=Food) # matrixs where the food is
		self.blobs = list(args) # stores the living blobs

	def set_food(self):
		self.food_board = np.empty((self.h, self.w), dtype=Food)
		for r in range(ceil(self.h*self.w/5)):
			x = np.random.randint(self.h)
			y = np.random.randint(self.w)
			self.food_board[x,y] = Food()

	def remove_food(self, position):
		x = position[0]
		y = position[1]
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

	def still_alive(self):
		for blob in self.blobs:
			if blob.nothing_todo == False:
				return True
		return False

	def cloning(self):
		for blob in self.blobs:
			new_blob = blob.clone()
			if new_blob != None:
				self.add_blob(new_blob)
				print('\t[log]:new blob')
			blob.reset()

	def remove_dead(self):
		for blob in self.blobs:
			if blob.dead == True:
				self.blobs.remove(blob)

	def draw_board(self):
		for i in range(self.h):
			for j in range(self.w):
				print('| |', end='') if self.food_board[i,j] == None else print('|f|', end='')
			print()

	def print_blobs(self):
		for i in self.blobs:
			print(i)

	def simulate(self, generation=1):
		for g in range(generation):
			print(f'generation number:{g}')
			while self.still_alive():
				for blob in self.blobs:
					while blob.is_moving and not blob.nothing_todo:
						print(blob)
						print('safe', blob.safe)
						print('dead', blob.dead)
						blob.move(self)
			self.remove_dead()
			self.cloning()
			self.draw_board()
			self.set_food()






