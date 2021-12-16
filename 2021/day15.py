def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	return[[int(i) for i in x.rstrip()] for x in lines]

class ChitonCave:

	def __init__(self, riskmap):
		self.risk = riskmap

		self.sizex = len(self.risk)
		self.sizey = len(self.risk[0])

	def tile_map(self, nx=5, ny=5):
		# instead, could just write a function to query risk when needed that calculates risk for any (i,j)
		self.sizex = nx*self.sizex
		self.sizey = ny*self.sizey

		newrisk = []

		for i in range(self.sizex):
			newrisk.append([(self.risk[i % len(self.risk)][j % (len(self.risk[0]))] + i // len(self.risk) + j // len(self.risk[0]) - 1) % 9 + 1 for j in range(self.sizey)])

		self.risk = newrisk

	def least_risk(self):

		# USE DIJKSTRA'S ALGORITHM
		inf = sum([x for row in self.risk for x in row ])
		dists = [[inf for _ in row] for row in self.risk]
		dists[0][0] = 0
		#prevs = [[None for _ in row] for row in self.risk] # if storing path

		import heapq # MY FIRST IMPORT?! TODO: write my own min heap?
		unvisited = [(0, (0,0))]

		while len(unvisited) > 0:

			risk, (i,j) = heapq.heappop(unvisited)

			if i==self.sizex-1 and j==self.sizey-1:
				return dists[i][j]

			neighbors = [(i-1,j), (i+1, j), (i, j-1), (i, j+1)]
			neighbors = [(x,y) for (x,y) in neighbors if x>=0 and y>=0 and x<self.sizex and y<self.sizey]

			for (x,y) in neighbors:
				newdist = risk + self.risk[x][y]
				if dists[x][y] is None or newdist < dists[x][y]:
					dists[x][y] = newdist
					heapq.heappush(unvisited,(newdist, (x,y)))
					#prevs[x][y] = (i,j)

if __name__ == "__main__":
	risk = load('./day15-input.txt')

	cave = ChitonCave(risk)

	print('Lowest possible risk:', cave.least_risk())

	cave.tile_map()

	print('Lowest possible risk after tiling 5x5:', cave.least_risk())