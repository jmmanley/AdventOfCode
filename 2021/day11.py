def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	return [[int(x) for x in line if x != '\n'] for line in lines]

class Octopi:

	def __init__(self, energy):
		self.energy = energy
		self.n_flashes = 0
		self.first_synchronous_step = False

	def step(self):

		flashed = [[False for _ in row] for row in self.energy]

		# increase all by 1
		self.energy = [[x+1 for x in row] for row in self.energy]

		def need_to_flash():
			return sum([self.energy[i][j]>9 and not flashed[i][j] for i in range(len(self.energy)) for j in range(len(self.energy[0]))])>0

		def flash(i,j):
			flashed[i][j] = True
			self.n_flashes += 1

			def increase_energy(i,j):
				if i>=0 and i<len(self.energy) and j>=0 and j<len(self.energy[0]):
					self.energy[i][j] += 1

			increase_energy(i-1,j)
			increase_energy(i-1,j-1)
			increase_energy(i-1,j+1)
			increase_energy(i,j-1)
			increase_energy(i,j+1)
			increase_energy(i+1,j)
			increase_energy(i+1,j-1)
			increase_energy(i+1,j+1)

		# check for flashes
		while need_to_flash():
			for i in range(len(self.energy)):
				for j in range(len(self.energy)):
					if self.energy[i][j]>9 and not flashed[i][j]:
						flash(i,j)

		# check if all flashed
		if sum([f for row in flashed for f in row]) == len(self.energy)*len(self.energy[0]):
			self.first_synchronous_step = True

		self.reset()

	def reset(self):
		for i in range(len(self.energy)):
			for j in range(len(self.energy)):
				if self.energy[i][j]>9: self.energy[i][j] = 0

	
if __name__ == "__main__":
	init_energies = load('./day11-input.txt')

	octopi = Octopi(init_energies)

	for _ in range(100):
		octopi.step()

	print('Number of flashes after 100 steps:', octopi.n_flashes)

	n_steps = 0

	octopi = Octopi(init_energies)

	while not octopi.first_synchronous_step:
		octopi.step()
		n_steps += 1

	print('Number of steps until first synchronous flash:', n_steps)