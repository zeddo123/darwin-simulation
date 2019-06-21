import argparse

from utils.env import Environement
from utils.blob import Blob
from utils.parser_help import *

from utils.plot import plot

parser = argparse.ArgumentParser(description=description)

parser.add_argument('-g', '--generations', metavar='N', type=int, help=generations_help)
parser.add_argument('--plot', nargs='+', type=str, help=plot_help, choices=choices_plot)

args = parser.parse_args()

if args.plot : args.plot = list(set(args.plot))
if args.generations == None: args.generations = 1

env = Environement(10,10,
	Blob(1,4,speed=12,size=3,energy=400,sense=1),
	Blob(9,0,speed=12,size=3,energy=400,sense=1, name='001'),
	Blob(8,3,speed=12,size=3,energy=400,sense=1, name='002'),
	Blob(1,4,speed=12,size=3,energy=400,sense=1, name='003'),
	Blob(9,0,speed=12,size=3,energy=400,sense=1, name='004'),
	Blob(8,6,speed=12,size=3,energy=400,sense=1, name='005'),
	Blob(1,4,speed=12,size=3,energy=400,sense=1, name='006'),
	Blob(9,4,speed=12,size=3,energy=400,sense=1, name='007'),
	Blob(8,9,speed=12,size=3,energy=400,sense=1, name='008')
)
print(env.blobs)
env.set_food()
env.draw_board()
env.simulate(args.generations)
env.print_blobs()

plot(env,args.plot)