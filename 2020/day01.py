def find2_sum(xs, target):
	# strategy: sort xs, then loop through list and look for 2020-xs[i]
	
	xs = sorted(xs)

	for x in xs:
		if target-x in xs:
			return (target-x) * x
	
	raise ValueError("No pair in the input sums to " + str(target))

def find3_sum(xs, target):
	# strategy: sort xs, the loop through list and use find2_sum(xs, 2020-xs[i])
	xs = sorted(xs)

	for i in range(len(xs)):
		try:
			result = xs[i] * find2_sum(xs[:i] + xs[i+1:], target-xs[i])
			return result
		except:
			continue

if __name__ == "__main__":
	input = open("day01-input.txt", "r")
	lines = input.readlines()
	xs = [int(x) for x in lines]
	target = 2020
	
	print('part 1, find 2 elements that sum to 2020 and multiply them:')
	print(find2_sum(xs, target))
	print(' ')

	print('part 2, find 3 elements that sum to 2020 and multiply them:')
	print(find3_sum(xs, target))
