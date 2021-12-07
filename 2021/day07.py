def fuel_needed_constant(positions, goal):
	return int(sum([abs(x-goal) for x in positions]))

def fuel_needed_notconstant(positions, goal):
	# Remember: sum of 1 to N is N(N+1)/2
	return int(sum([abs(x-goal)*(abs(x-goal)+1)/2 for x in positions]))

def median(x):
	x = sorted(x)
	mid = int(len(x)/2)
	if len(x) % 2 == 0:
		return (x[mid-1]+x[mid])/2
	else:
		return x[mid]

def load(txt):
	with open(txt) as file:
		data = file.readline()

	return [int(x) for x in data.split(',')]

if __name__ == "__main__":
	positions = load('./day07-input.txt')

	# BRUTE FORCE: try all positions within range
	#fuels = [fuel_needed_constant(positions, goal) for goal in range(min(positions), max(positions)+1)]

	# Better solution: this constant fuel is minimized by the MEDIAN of the positions

	print('Minimum fuel at constant rate:', fuel_needed_constant(positions, median(positions)))


	# A better solution for the not constant solution may be to search around the mean of the values, but 
	# not immediately clear to me how wide we expect the variation around the mean to be

	fuels = [fuel_needed_notconstant(positions, goal) for goal in range(min(positions), max(positions)+1)]

	print('Minimum fuel at increasing rate:', min(fuels))