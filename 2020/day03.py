def count_trees(map, right, down):
	# assume map is an array of strings
	
	i = 0
	j = 0
	w = len(map[0])
	h = len(map)
	
	if map[i][j] == '#': count = 1
	else:               count = 0
	
	while i+down < h:
		i = i+down
		j = (j+right) % (w-1)
		
		if map[i][j] == '#': count += 1
	
	return count

if __name__ == "__main__":
	input = open('day03-input.txt','r')
	map = input.readlines()
	
	print('part 1, count number of trees with slope right 3, down 1:')
	print(count_trees(map, 3, 1))

	print('part 2, count many slopes and multiply:')
	from utils import prod
	print(prod([count_trees(map, slope[0], slope[1]) for slope in [(1,1),(3,1),(5,1),(7,1),(1,2)]]))
