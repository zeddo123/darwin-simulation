import unittest
from ../blob import Blob

class TestBlob(unittest.TestCase):
	"""unittest TestBlob"""
	def setUp(self):
		self.blob = Blob(1,1,speed=12,size=3,energy=400,sense=2)

	def test_go_to_values(self):
		self.blob.go_to((5, 5))
		self.assertAlmostEqual((self.x, self.y), (5,5))

		self.assertRaises(ValueError, self.blob.go_to, (0,-1))
		self.assertRaises(ValueError, self.blob.go_to, (-1,0))

	def test_go_to_types(self):
		# test type for tuple with more than two elements
		self.assertRaises(TypeError, self.blob.go_to, (7,6, 5))

		# test type for sting tuple 
		self.assertRaises(TypeError, self.blob.go_to, ('51','516'))
		
		# test type for tuple of tuple
		self.assertRaises(TypeError, self.blob.go_to, (3,(3,)))
		self.assertRaises(TypeError, self.blob.go_to, ((5,),3))

	def test_senseable_values(self):
		# blob position (1, 1)
		self.assertAlmostEqual(self.blob.senseable(2,2), True)
		self.assertAlmostEqual(self.blob.senseable(4,4), False)
		self.assertAlmostEqual(self.blob.senseable(1,1), True)

		self.assertRaises(ValueError, self.blob.senseable, -1, 0)

