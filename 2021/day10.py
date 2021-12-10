def load(txt):
	with open(txt) as file:
		lines = file.readlines()
	lines = [x.rstrip() for x in lines]
	return lines

def score_errors(line):
	# Use a stack to keep track of the most recent open parenthesis

	# DEFINE SOME CONSTANTS
	points = dict()
	points[')'] = 3
	points[']'] = 57
	points['}'] = 1197
	points['>'] = 25137

	opens = ['(', '[', '{', '<']
	close = [')', ']', '}', '>']

	def flip(x):
		return [close[i] for i in range(len(opens)) if x==opens[i]][0]

	stack = []

	for x in line:
		if x in opens:
			# Add open character to top of stack
			stack.append(x)
		elif flip(stack[-1]) == x:
			# Correct close character - remove from top of stack
			stack = stack[:-1]
		else:
			# ERROR!
			return points[x]

	return 0


def score_completions(line):
	# Use a stack to keep track of the most recent open parenthesis

	# DEFINE SOME CONSTANTS
	points = dict()
	points[')'] = 1
	points[']'] = 2
	points['}'] = 3
	points['>'] = 4

	opens = ['(', '[', '{', '<']
	close = [')', ']', '}', '>']

	def flip(x):
		return [close[i] for i in range(len(opens)) if x==opens[i]][0]

	# Sorry for copy/pasted code! Should refactor these two functions.
	stack = []

	for x in line:
		if x in opens:
			# Add open character to top of stack
			stack.append(x)
		elif flip(stack[-1]) == x:
			# Correct close character - remove from top of stack
			stack = stack[:-1]
		else:
			# ERROR!
			return None

	# Now score completion!
	score = 0
	for i in range(len(stack)):
		score = score*5 + points[flip(stack[-i-1])]

	return score

if __name__ == "__main__":
	lines = load('./day10-input.txt')

	error_scores = [score_errors(x) for x in lines]
	total_error_score = sum(error_scores)

	print('Total syntax error score:', total_error_score)

	incomplete_lines = [lines[i] for i in range(len(lines)) if error_scores[i]==0]
	completion_scores = [score_completions(x) for x in incomplete_lines]

	from day07 import median
	print('Middle completion score:', median(completion_scores))

