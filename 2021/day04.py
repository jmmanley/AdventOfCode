class BingoCard:
	# Class to represent a bingo card board and perform various
	# actions to play a bingo game

	def __init__(self, board):
		self.board = board
		self.size = len(board) # assume square board
		self.marked = [[False for _ in range(self.size)] for _ in range(self.size)]

		self.latest_number = None # used for score calculation
		self.i_won = False

	def mark(self, number):
		# Checks if number exists in board and, if so, marks that position
		# Returns True if that mark makes you a winner! Otherwise, False

		if self.i_won:
			# Finished playing - only BINGO! the first time
			return False

		self.latest_number = number
		found = False

		for i in range(self.size):
			for j in range(self.size):
				if self.board[i][j] == number:
					self.marked[i][j] = True
					found = True
					break

			if found:
				break

		# Check if you are a winner!
		return self.have_i_won(i, j)

	def have_i_won(self, i, j):
		# Check for a win in the ith row
		if all([self.marked[i][jj] for jj in range(self.size)]): 
			self.i_won = True
			return True

		# Check for a win in the jth column
		if all([self.marked[ii][j] for ii in range(self.size)]): 
			self.i_won = True
			return True

		# Note: diagonals do NOT win!
		return False

	def score(self):
		# Grab all unmarked numbers
		unmarked = [self.board[i][j] for i in range(self.size) for j in range(self.size) if not self.marked[i][j]]

		return sum(unmarked) * self.latest_number


def load(txt, boardsize=5):
	with open(txt) as file:
		lines = file.readlines()

	lines = [x for x in lines if x != '\n'] # remove blank lines

	sequence = lines[0] # save random number sequence
	sequence = [int(x) for x in sequence.split(',')] # convert to list of ints

	lines = lines[1:]

	boards = []

	for i in range(int(len(lines)/boardsize)):
		curr = lines[i*boardsize:(i+1)*boardsize] # get current board

		# convert string for each row into list of integers
		board = [[int(x) for x in line.split(' ') if x != ''] for line in curr]

		boards.append(BingoCard(board))

	return sequence, boards
		



if __name__ == "__main__":
	sequence, boards = load('./day04-input.txt')

	first_score = None
	final_score = None
	n_won = 0

	for n in sequence:
		# iterate over all boards and mark, checking if won along the way

		for board in boards:
			if board.mark(n):
				# BINGO!

				if first_score is None:
					# check if it's the first winner
					first_score = board.score()

				n_won += 1

				if n_won == len(boards):
					# check if it's the last winner
					final_score = board.score()
					break

		if n_won == len(boards):
			break
				

	print('first winning score:', first_score)

	print('last winning score:', final_score)

