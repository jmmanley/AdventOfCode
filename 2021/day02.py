def load(txt):
	with open(txt) as file:
		return file.readlines()

if __name__ == "__main__":
	directions = load('./day02-input.txt')

	horizontal = 0
	aim        = 0
	depth      = 0  # first rules
	depth_aim  = 0  # second rules

	for d in directions:
		direction, n = d.split(' ')
		n = int(n)

		if direction == 'forward':
			horizontal += n
			depth_aim += aim*n
		elif direction == 'up':
			depth -= n
			aim   -= n
		elif direction == 'down':
			depth += n
			aim   += n
		else:
			raise ValueError('input not recognized!')

	print('product of final horizontal position and depth:', depth*horizontal)

	print('product of final horizontal position and depth with aim:', depth_aim*horizontal)
