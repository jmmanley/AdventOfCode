class LanternSwarm:

	def __init__(self, init_timers):
		self.nfish_by_timer = [0 for _ in range(9)]

		for x in init_timers:
			self.nfish_by_timer[x] += 1

	def a_day_passes(self):
		n_reproduce = self.nfish_by_timer[0]

		for i in range(1,9):
			self.nfish_by_timer[i-1] = self.nfish_by_timer[i]

		self.nfish_by_timer[6] += n_reproduce
		self.nfish_by_timer[8] = n_reproduce

	def fast_forward(self, days):
		for _ in range(days):
			self.a_day_passes()

	def population(self):
		return sum(self.nfish_by_timer)

def load(txt):
	with open(txt) as file:
		line = file.readline()

	return [int(x) for x in line.split(',')]

if __name__ == "__main__":
	init_timers = load('./day06-input.txt')

	swarm = LanternSwarm(init_timers)
	swarm.fast_forward(80)

	print('Number of lanternfish after 80 days:', swarm.population())

	swarm.fast_forward(256-80)

	print('Number of lanternfish after 256 days:', swarm.population())