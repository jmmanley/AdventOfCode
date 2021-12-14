def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	return lines

class LightGrid:

	def __init__(self, gridsize=1000):
		self.grid = [[False for _ in range(gridsize)] for _ in range(gridsize)]

	def follow_instruction(self, instruction):
		parts = instruction.split(' ')
		todo = ' '.join(parts[:-3])
		pos1 = parts[-3]
		pos2 = parts[-1]

		pos1 = [int(x) for x in pos1.split(',')]
		pos2 = [int(x) for x in pos2.split(',')]

		if todo == 'turn on':
			self.turn_on(pos1, pos2)
		elif todo == 'turn off':
			self.turn_off(pos1, pos2)
		elif todo == 'toggle':
			self.toggle(pos1, pos2)

	def turn_on(self, pos1, pos2):
		for i in range(pos1[0], pos2[0]+1):
			for j in range(pos1[1], pos2[1]+1):
				self.grid[i][j] = True

	def turn_off(self, pos1, pos2):
		for i in range(pos1[0], pos2[0]+1):
			for j in range(pos1[1], pos2[1]+1):
				self.grid[i][j] = False

	def toggle(self, pos1, pos2):
		for i in range(pos1[0], pos2[0]+1):
			for j in range(pos1[1], pos2[1]+1):
				self.grid[i][j] = not self.grid[i][j]

	def n_lit(self):
		return sum([sum(x) for x in self.grid])


class ContinuousLightGrid:

	def __init__(self, gridsize=1000):
		self.grid = [[0 for _ in range(gridsize)] for _ in range(gridsize)]

	def follow_instruction(self, instruction):
		parts = instruction.split(' ')
		todo = ' '.join(parts[:-3])
		pos1 = parts[-3]
		pos2 = parts[-1]

		pos1 = [int(x) for x in pos1.split(',')]
		pos2 = [int(x) for x in pos2.split(',')]

		if todo == 'turn on':
			self.turn_on(pos1, pos2)
		elif todo == 'turn off':
			self.turn_off(pos1, pos2)
		elif todo == 'toggle':
			self.toggle(pos1, pos2)

	def turn_on(self, pos1, pos2):
		for i in range(pos1[0], pos2[0]+1):
			for j in range(pos1[1], pos2[1]+1):
				self.grid[i][j] += 1

	def turn_off(self, pos1, pos2):
		for i in range(pos1[0], pos2[0]+1):
			for j in range(pos1[1], pos2[1]+1):
				self.grid[i][j] = max(0, self.grid[i][j]-1)

	def toggle(self, pos1, pos2):
		for i in range(pos1[0], pos2[0]+1):
			for j in range(pos1[1], pos2[1]+1):
				self.grid[i][j] += 2

	def brightness(self):
		return sum([sum(x) for x in self.grid])

if __name__ == "__main__":
	instructions = load('./day06-input.txt')

	lights = LightGrid()

	for i in instructions:
		lights.follow_instruction(i)

	print('Number of lights that are on:', lights.n_lit())

	continuous_lights = ContinuousLightGrid()

	for i in instructions:
		continuous_lights.follow_instruction(i)

	print('Total brightness:', continuous_lights.brightness())