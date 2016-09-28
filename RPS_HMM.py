"""Simple AI that plays rock paper scissors by modeling the user's sequential
moves as a hidden markov model and making predictions on what the next move 
will likely be"""
import computer_player as comp

#stats we'll display at the end of the game
p_wins = 0
cp_wins = 0
ties = 0
# permanent int assignments for all three moves
ROCK = 0
PAPER = 1
SCISSORS = 2
#conversions between string and int representations of moves
s2int_move = {'r' : 0 , 'p' : 1 , 's' : 2}
int2s_move = {0 : 'Rock' , 1 : "Paper" , 2 : 'Scissors'}
# 0 is loss, 1 is win, 2 is tie
find_winner = {
ROCK: {ROCK:2, PAPER:0, SCISSORS:1}, 
PAPER: {ROCK:1, PAPER:2, SCISSORS:0}, 
SCISSORS:{ROCK:0, PAPER:1, SCISSORS:2}}

def win():
	print "You won!"
	global p_wins
	p_wins += 1

def lose():
	print "You lose"
	global cp_wins 
	cp_wins += 1

def tie():
	print "You tied"
	global ties
	ties += 1

results = {0:lose, 1:win, 2:tie}

def main():

	cp = comp.computer_player()
	print "Input \'r\' to play Rock \'p\' to play Paper \'s\' to play " \
	"Scissors, or \'q\' to quit."
	play = True

	while play:
		player_move = raw_input("Enter your next move: ")
		

		if player_move == 'q':
			play = False
		else:
			cp_move = cp.play()
			winner = find_winner[s2int_move[player_move]][cp_move]

			# Tell player who won, update win stats
			print "Computer played ", int2s_move[cp_move]
			results[winner]()

			cp.see(s2int_move[player_move])

	print "Player Wins: ", p_wins
	print "Computer Wins: ", cp_wins
	print "Ties: ", ties

if __name__ == "__main__":
	main()