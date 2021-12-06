def find_sum_pair(xs, goal):
	for x in xs:
		if (goal-x) in xs: return True
	
	return False

def find_not_nprev_sum(xs, n=25):
	for i in range(26, len(xs)):
		if not find_sum_pair(xs[i-25-1:i], xs[i]):
			return xs[i]

def find_contiguous_sum(xs, goal):
	imin = 0
	imax = 1
	
	curr_sum = xs[0]

	while curr_sum != goal:
		if curr_sum < goal:
			imax += 1
		else:
			imin += 1
		
		curr_sum = sum(xs[imin:imax])
	
	return xs[imin:imax]
		
if __name__ == "__main__":
	with open('day09-input.txt') as f:
		lines = f.readlines()
	
	xs = [int(x) for x in lines]
	
	print('part 1, first number that is not a sum of pair in previous 25 values:')
	n = find_not_nprev_sum(xs)
	print(n)

	print('part 2, find encryption weakness:')
	xmas = find_contiguous_sum(xs,n)
	print(min(xmas) + max(xmas))
