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
		self.sizex = nx*self.sizex
		self.sizey = ny*self.sizey

		newrisk = []

		for i in range(self.sizex):
			newrisk.append([(self.risk[i % len(self.risk)][j % (len(self.risk[0]))] + i // len(self.risk) + j // len(self.risk[0]) - 1) % 9 + 1 for j in range(self.sizey)])

		self.risk = newrisk

	# WORKS FOR PART 1 BUT NOT PART 2
	# def least_risk(self):

	# 	# USE DIJKSTRA'S ALGORITHM
	# 	inf = sum([x for row in self.risk for x in row ])
	# 	dists = [[inf for _ in row] for row in self.risk]
	# 	dists[0][0] = 0
	# 	prevs = [[None for _ in row] for row in self.risk]
	# 	unvisited = [(i,j) for i in range(self.sizex) for j in range(self.sizey)]
	# 	unvisited_dists = [dists[i][j] for i in range(self.sizex) for j in range(self.sizey)]

	# 	while len(unvisited) > 0:

	# 		(i,j) = unvisited[0]

	# 		if i==self.sizex-1 and j==self.sizey-1:
	# 			return dists[i][j]

	# 		unvisited_dists = unvisited_dists[1:]
	# 		unvisited = unvisited[1:]

	# 		neighbors = [(i-1,j), (i+1, j), (i, j-1), (i, j+1)]
	# 		neighbors = [(x,y) for (x,y) in neighbors if x>=0 and y>=0 and x<self.sizex and y<self.sizey and (x,y) in unvisited]

	# 		for (x,y) in neighbors:
	# 			newdist = dists[i][j] + self.risk[x][y]
	# 			if dists[x][y] is None or newdist < dists[x][y]:
	# 				dists[x][y] = newdist
	# 				prevs[x][y] = (i,j)

	# 		def argsort(x):
	# 			return sorted(range(len(x)), key=x.__getitem__)

	# 		# this sorting problem is not too bad because only a few elements will move each time
	# 		# and they may be roughly in order
	# 		idx = argsort(unvisited_dists)
	# 		unvisited_dists = [unvisited_dists[i] for i in idx]
	# 		unvisited = [unvisited[i] for i in idx]

	# 		# Ideal solution: storing unvisited in a min heap

	def least_risk(self):

		# USE DIJKSTRA'S ALGORITHM
		inf = sum([x for row in self.risk for x in row ])
		dists = [[inf for _ in row] for row in self.risk]
		dists[0][0] = 0
		#prevs = [[None for _ in row] for row in self.risk] # if storing path

		import heapq
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



	# 	def traverse(i, j, path, minscore, currscore):
	# 		# THIS SOLUTION IS NOT EFFICIENT. NEED A MORE OPTIMAL PATH FINDING ALGORITHM
	# 		# LIKE DIJKSTRA!
	# 		if i==self.sizex-1 and j==self.sizey-1:
	# 			# REACHED THE END!
	# 			if minscore is None:
	# 				minscore = currscore
	# 			else:
	# 				minscore = min(currscore, minscore)
	# 		else:
	# 			neighbors = [(i-1,j), (i+1, j), (i, j-1), (i, j+1)]
	# 			neighbors = [(x,y) for (x,y) in neighbors if x>=0 and y>=0 and x<self.sizex and y<self.sizey and (x,y) not in path]

	# 			risks = [self.risk[x][y] for (x,y) in neighbors]

	# 			def argsort(x):
	# 				return sorted(range(len(x)), key=x.__getitem__)

	# 			neighbors = [neighbors[i] for i in argsort(risks)]

	# 			for (x,y) in neighbors:
	# 				def lessOrNone(x,y):
	# 					if x is None or y is None:
	# 						return True
	# 					else:
	# 						return x < y
	# 				if lessOrNone(currscore+self.risk[x][y], minscore):
	# 					minscore = traverse(x, y, path+[(x,y)], minscore, currscore+self.risk[x][y])

	# 		return minscore

	# 	naive_score = sum([self.risk[0][j] for j in range(1,self.sizey)]) + sum([self.risk[i][-1] for j in range(1,self.sizex)])

	# return traverse(0,0, [(0,0)], naive_score, 0)

if __name__ == "__main__":
	risk = load('./day15-input.txt')

	cave = ChitonCave(risk)

	from time import time

	start = time()
	print('Lowest possible risk:', cave.least_risk())
	print(time()-start)

	cave.tile_map()

	start = time()
	print('Lowest possible risk after tiling 5x5:', cave.least_risk())
	print(time()-start)