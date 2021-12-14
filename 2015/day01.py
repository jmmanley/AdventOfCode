def load(txt):
	with open(txt) as file:
		line = file.readline()

	return line

def step(x):
	if x == '(':
		return 1
	elif x == ')':
		return -1

def climb_floors(input):
	floor = 0

	for x in input:
		floor += step(x)

	return floor

def how_long_until_basement(input):
	floor = 0
	n = 0

	for x in input:
		floor += step(x)
		n += 1

		if floor == -1:
			return n

if __name__ == "__main__":
	instructions = load('./day01-input.txt')

	floor = climb_floors(instructions)

	print('The instructions take Santa to floor:', floor)

	basement_position = how_long_until_basement(instructions)

	print('Santa first enters the basement at position:', basement_position)