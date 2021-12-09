def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	return [[int(x) for x in line if x != '\n']  for line in lines]

def is_local_minimum(x, i, j):
	n = x[i][j]

	if (i==0 or x[i-1][j]>n) and \
	   (i==len(x)-1 or x[i+1][j]>n) and \
	   (j==0 or x[i][j-1]>n) and \
	   (j==len(x[i])-1 or x[i][j+1]>n):
		return True
	else:
		return False

def prod(x):
	if len(x)==0:
		return 1
	else:
		return x[0] * prod(x[1:])

def basin_size(x, i, j, visited=None):
	# Starting from a known point (i,j) in a basin, traverses the neighbors
	# and counts the total size of the basin in a recursive fashion

	if visited is None:
		# Need to mark positions as "visited" to prevent infinite recursion
		visited = [[False for _ in range(len(x))] for _ in range(len(x[0]))]

	if i<0 or j<0 or i>=len(x) or j>=len(x[i]) or visited[i][j] or x[i][j] == 9:
		return 0

	visited[i][j] = True

	return 1 + basin_size(x,i-1,j,visited) + basin_size(x,i+1,j,visited) + basin_size(x,i,j-1,visited) + basin_size(x,i,j+1,visited)

if __name__ == "__main__":
	heightmap = load('./day09-input.txt')

	local_minima = []

	for i in range(len(heightmap)):
		for j in range(len(heightmap[0])):
			if is_local_minimum(heightmap, i, j): 
				local_minima.append([i,j])

	sum_risks = sum([heightmap[ij[0]][ij[1]] + 1 for ij in local_minima])

	print('Sum of risk scores of all local minima:', sum_risks)

	basin_sizes = sorted([basin_size(heightmap, ij[0], ij[1]) for ij in local_minima])

	print('Product of 3 largest basin sizes:', prod(basin_sizes[-3:]))