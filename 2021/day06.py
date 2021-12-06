class LanternSwarm:

	def __init__(self, init_timers):
		self.timers = init_timers # store all timers in a list

	def a_day_passes(self):
		curr_size = len(self.timers)

		for i in range(curr_size):
			if self.timers[i] == 0:
				self.timers[i] = 6
				self.timers.append(8)
			else:
				self.timers[i] -= 1

	def fast_forward(self, days):
		for _ in range(days):
			self.a_day_passes()
			print(self.timers)

	def population(self):
		return len(self.timers)

def load(txt):
	with open(txt) as file:
		line = file.readline()

	return [int(x) for x in line.split(',')]

if __name__ == "__main__":
	init_timers = load('./day06-input.txt')

	swarm = LanternSwarm(init_timers)

	swarm.fast_forward(80)

	print('Number of lanternfish after 80 days:', swarm.population())

	# #swarm.fast_forward(256-80) # THIS IS HARD TO DO NUMERICALLY DO TO EXPONENTIAL GROWTH