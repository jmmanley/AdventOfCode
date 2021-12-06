def play(instructions):
	acc = 0
	visited = dict()
	curr = 0

	while curr not in visited.keys() and curr < len(instructions):
		instruct = instructions[curr]
		todo = instruct[:3]
		n = int(instruct[4:])
		visited[curr] = True
		
		if todo == 'nop': curr += 1
		if todo == 'acc':
			acc  += n
			curr += 1
		if todo == 'jmp':
			curr += n
	return acc, max(visited.keys())

if __name__ == "__main__":
	with open('day08-input.txt') as f:
		instructions = f.readlines()
	
	print('part 1, accumulator value at time of first repeat execution:')
	acc, max_visited = play(instructions)
	print(acc)
	print(max_visited)
	
	print('part 2, accumulator value after fixing loop:')
	instructions[max_visited] = 'nop +0'
	print(len(instructions))
	print(play(instructions))
