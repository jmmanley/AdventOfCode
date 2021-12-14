def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	return [x.rstrip().split('-') for x in lines]

class Caves:

	def __init__(self, neighbors):
		self.neighbors = dict()

		for x in neighbors:
			if x[0] not in self.neighbors.keys():
				self.neighbors[x[0]] = [x[1]]
			else:
				self.neighbors[x[0]].append(x[1])

			if x[1] not in self.neighbors.keys():
				self.neighbors[x[1]] = [x[0]]
			else:
				self.neighbors[x[1]].append(x[0])

	def n_paths(self):
		# TRAVERSE PATHS
		visited = dict()
		for x in self.neighbors.keys():
			visited[x] = False

		def count_paths(pos, visited):
			n = 0
			visited = visited.copy() # Problem was the recursive overwrites were being carried over!
			visited[pos] = True
			for x in self.neighbors[pos]:
				if x == 'end':
					n+=1
				elif not visited[x] or x.isupper():
					n+=count_paths(x, visited)
			return n

		return count_paths('start', visited)

	def n_paths_twice_small(self):
		# TRAVERSE PATHS
		visited = dict()
		for x in self.neighbors.keys():
			visited[x] = 0

		def count_paths(pos, visited):
			n = 0
			visited = visited.copy() # Problem was the recursive overwrites were being carried over!
			if pos.islower(): 
				visited[pos] += 1
			
			for x in self.neighbors[pos]:
				if x == 'start':
					continue
				elif x == 'end':
					n+=1
				elif x.isupper() or visited[x]==0:
					n+=count_paths(x, visited)
				elif (x.islower() and visited[x]==1 and (2 not in visited.values())):
					n+=count_paths(x, visited)

			return n

		return count_paths('start', visited)

if __name__ == "__main__":
	neighbors = load('./day12-input.txt')

	caves = Caves(neighbors)

	print('Number of distinct paths:', caves.n_paths())
	print('Number of distinct paths if we visit a single small cave twice:', caves.n_paths_twice_small())
