def parse_input(file):
	groups = []
	counts = []
	with open(file) as input:
		line = input.readline()
		curr = dict()
		count = 0
		while line:
			if line == '\n':
				groups.append(curr)
				counts.append(count)
				curr = dict()
				count = 0
			else:
				for x in line:
					if ord(x)>96 and ord(x)<123:
						if x in curr.keys(): curr[x] += 1
						else: curr[x] = 1
				count += 1
			
			line = input.readline()
		
		groups.append(curr)
		counts.append(count)
	
	return groups, counts


if __name__ == "__main__":
	groups, counts = parse_input('day06-input.txt')	
	print(counts)
	print('part 1, sum of group counts:')
	print(sum([len(group.keys()) for group in groups]))

	print('part 2, sum of group counts:')
	print(sum([sum([x == counts[i] for x in groups[i].values()]) for i in range(len(groups))])) # simplify this
