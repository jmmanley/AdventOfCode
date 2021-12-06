class BingoCard:

	def __init__(self, board):
		self.board = board

def load(txt, boardsize=5):
	with open(txt) as file:
		lines = file.readlines()

	lines = len([x for x in lines if x != '\n'])

	sequence = lines[0]

	lines = lines[1:]

	for i in range(len(lines)/boardsize):
		curr = lines[i*boardsize:(i+1)*boardsize]

if __name__ == "__main__":
	load('./day04-input.txt')