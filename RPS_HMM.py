"""Simple AI that plays rock paper scissors by modeling the user's sequential
moves as a hidden markov model and making predictions on what the next move 
will likely be"""

#Hi, Andy

import random

# permanent int assignments for all three moves
ROCK = 0
PAPER = 1
SCISSORS = 2
s2int_move = {'r' : 0 , 'p' : 1 , 's' : 2}
int2s_move = {0 : 'Rock' , 1 : "Paper" , 2 : 'Scissors'}



class computer_player:
	prev = -1
	data = []

	def __init__(self):
		# construct basic 2D array to hold records of players moves
		# 0 index entry of move_data is how many times player threw rock after throwing move
		# 1 index entry is how many times player threw paper, 2 index is scissors
		# 3 index is how many observations following a move throw have been made
		rock_data = [1,1,1,3]
		paper_data = [1,1,1,3]
		scissors_data = [1,1,1,3]
		self.data.append(rock_data)
		self.data.append(paper_data)
		self.data.append(scissors_data)

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



def find_winner(player_move, cp_move):
	# 0 is a player loss
	# 1 is a player win
	# 2 is a tie
	if player_move == ROCK:
		if cp_move == ROCK:
			return 2
		elif cp_move == PAPER:
			return 0
		elif cp_move == SCISSORS:
			return 1
	elif player_move == PAPER:
		if cp_move == ROCK:
			return 1
		elif cp_move == PAPER:
			return 2
		elif cp_move == SCISSORS:
			return 0
	elif player_move == SCISSORS:
		if cp_move == ROCK:
			return 0
		elif cp_move == PAPER:
			return 1
		elif cp_move == SCISSORS:
			return 2



def main():
	p_wins = 0
	cp_wins = 0
	ties = 0
	cp = computer_player()
	print "Input \'r\' to play Rock \'p\' to play Paper \'s\' to play " \
	"Scissors, or \'q\' to quit."
	play = True

	while play:
		player_move = raw_input("Enter your next move: ")
		cp_move = cp.play()

		if player_move == 'q':
			play = False
		else:
			winner = find_winner(s2int_move[player_move],cp_move)

			#Tell player who won, update win stats
			print "Computer played ", int2s_move[cp_move]
			if winner == 0:
				print "You lost."
				cp_wins += 1
			elif winner == 1:
				print "You won!"
				p_wins += 1
			elif winner == 2:
				print "You tied."
				ties += 1


			cp.see(s2int_move[player_move])

	print "Player Wins: ", p_wins
	print "Computer Wins: ", cp_wins
	print "Ties: ", ties



if __name__ == "__main__":
	main()
