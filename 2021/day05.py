class VentCounter:

	def __init__(self, size=10, horizontal=True):
		self.size = size
		self.horizontal = horizontal # whether or not to ONLY consider vertical/horizontal lines

		# initialize with zero vents
		self.vents = [[0 for _ in range(self.size)] for _ in range(self.size)]

	def add_vents(self, linepair):
		minx = min(linepair[0][0], linepair[1][0])
		maxx = max(linepair[0][0], linepair[1][0])

		miny = min(linepair[0][1], linepair[1][1])
		maxy = max(linepair[0][1], linepair[1][1])

		if minx==maxx or miny==maxy:
			# COUNT HORIZONTAL OR VERTICAL LINES
			for i in range(minx,maxx+1):
				for j in range(miny,maxy+1):
					self.vents[i][j] += 1

		elif not self.horizontal:
			# ALSO COUNT 45 DEGREE LINES IF NOTED
			for (i,j) in zip(myrange(linepair[0][0], linepair[1][0]), 
				             myrange(linepair[0][1], linepair[1][1])):
				self.vents[i][j] += 1

	def count_dangerous(self, min_vents=2):

		n_dangerous = 0

		for i in range(self.size):
			for j in range(self.size):
				if self.vents[i][j] >= min_vents:
					n_dangerous += 1

		return n_dangerous

def myrange(start, stop):
	# a range that is inclusive of stop and automatically decrements if necessary
	if start > stop:
		return range(start,stop-1,-1)
	else:
		return range(start,stop+1)

def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	linepairs = []

	for line in lines:
		x = line.split(' ')

		linepairs.append([[int(n) for n in x[i].split(',')] for i in [0,2]])

	return linepairs

if __name__ == "__main__":
	linepairs = load('./day05-input.txt')

	# built grid the size of largest position in line pairs
	size = max([n for pair in linepairs for x in pair for n in x])+1

	vents_horizontal = VentCounter(size, horizontal=True)
	vents_all = VentCounter(size, horizontal=False)

	for linepair in linepairs:
		vents_horizontal.add_vents(linepair)
		vents_all.add_vents(linepair)

	print('Number of dangerous points (>=2 vents), horizontal/vertical only:', vents_horizontal.count_dangerous())

	print('Number of dangerous points (>=2 vents), all lines:', vents_all.count_dangerous())


