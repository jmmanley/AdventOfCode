def load(txt):
	with open(txt) as file:
		line = file.readline()

	return line

class SantasMap:

	def __init__(self):
		self.x = 0
		self.y = 0

		self.map = dict()
		self.map[(0,0)] = 1

	def take_step(self, step):
		if step == '>':
			self.x += 1
		elif step == '<':
			self.x -= 1
		elif step == '^':
			self.y += 1
		elif step == 'v':
			self.y -= 1

		if (self.x, self.y) not in self.map.keys():
			self.map[(self.x, self.y)] = 1
		else:
			self.map[(self.x, self.y)] += 1

	def n_visited(self):
		return len(self.map.keys())

	def add_map(self, santaMap):
		for pos in santaMap.map.keys():
			if pos not in self.map.keys():
				self.map[pos] = santaMap.map[pos]
			else:
				self.map[pos] += santaMap.map[pos]


if __name__ == "__main__":
	directions = load('./day03-input.txt')

	map = SantasMap()
	robomap = SantasMap()

	for step in directions:
		map.take_step(step)

	print('Number of houses visited by Santa:', map.n_visited())

	santaMap = SantasMap()
	roboMap  = SantasMap()

	i = 0

	for step in directions:
		if i % 2 == 0:
			santaMap.take_step(step)
		else:
			roboMap.take_step(step)
		i += 1

	# Santa gets all the credit
	santaMap.add_map(roboMap)

	print('Number of houses visited by Santa AND Robo-Santa:', santaMap.n_visited())