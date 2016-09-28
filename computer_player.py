#Computer player class for RPS game

import random
import numpy as np

class computer_player:
	prev = -1
	data = []

	def __init__(self):
		# construct basic 2D array to hold records of players moves
		# data[i] is an array holding records of players moves after move i
		# data[i][k] holds number of times k was played after i for k=0,1,2
		# data[i][3] holds total number of moves played after i
		turn_has_passed = False
		self.data = np.ones((3,4))
		for i in range(0,len(self.data)):
			self.data[i][-1] = 3

	#make move based on opponents previous moves
	def play(self):
		rock = self.data[self.prev][0]
		paper = self.data[self.prev][1]
		scissors = self.data[self.prev][2]
		total = self.data[self.prev][3]

		rp = rock/float(total)
		pp = rp + paper/float(total)
		sp = pp + scissors/float(total) #should be 1.00

		move = random.uniform(0,1)

		# throw paper as frequently as rock is expected to be thrown
		# scissors as frequently as paper, and rock as scissors
		if move < rp:
			return 1
		elif move < pp:
			return 2
		else:
			return 0


	#computer player sees oponents last move, updates data
	def see(self, curr):
		self.update(curr,self.prev)
		self.prev = curr

	#update hmm data
	def update(self, curr, prev):
		if prev != -1:
			self.data[prev][curr] +=1
			self.data[prev][3] += 1