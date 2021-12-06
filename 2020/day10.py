def find_chain(xs, goal=None):
	xs = sorted(xs)
	if goal is None: goal = xs[-1] + 3

	xs = [0] + xs + [goal]
	
	from utils import diff
	
	return diff(xs)

def find_possible_chains(xs):
	if len(xs) < 3: return 0
	
	if xs[2]-xs[0] < 4:

if __name__ == "__main__":
	with open('day10-input.txt') as f:
		input = f.readlines()

	xs = [int(x) for x in input]
	
	print('part 1, number of 1-jolt diffs * number of 3-jolt diffs:')
	chain = find_chain(xs)
	print(sum([x == 1 for x in chain]) * sum([x == 3 for x in chain]))
	
	print('part 2, number of possible chains:')
	print(find_possible_chains(xs))
