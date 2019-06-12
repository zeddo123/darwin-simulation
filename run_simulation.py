from utils.env import Environement
from utils.blob import Blob

env = Environement(10,10,
	Blob(1,4,speed=12,size=3,energy=4,sense=1),
	Blob(9,0,speed=12,size=3,energy=4,sense=1, name='001'),
	Blob(8,3,speed=12,size=3,energy=4,sense=1, name='002')
	)
print(env.blobs)
env.set_food()
env.draw_board()
env.simulate(2)
env.print_blobs()