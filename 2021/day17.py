def load(txt):
	with open(txt) as file:
		line = file.readline()

	parts = line.split('=')

	x = parts[1].split('..')
	x = [int(n.strip(', y')) for n in x]

	y = parts[2].split('..')
	y = [int(n.rstrip()) for n in y]

	return x, y


def naive_search(target):
	if target[0][0]<0:
		negx = -1
	else:
		negx = 1

	hs = []
	vels = []
	maxy = max([abs(x) for x in target[1]])
	for vx in range(max([abs(x) for x in target[0]])+1):
		for vy in range(-maxy, maxy+1):

			currh = throw(negx*vx, vy, target)

			if currh is not None:
				hs.append(currh)
				vels.append((vx,vy))

	return hs, vels


def throw(vx, vy, target):
	pos = [0,0]

	maxh = 0

	while still_possible(pos, vx, vy, target):
		pos[0] += vx
		pos[1] += vy

		if pos[1] > maxh:
			maxh = pos[1]

		if   vx<0: vx += 1
		elif vx>0: vx -= 1

		vy -= 1

	if inrange(pos[0],target[0]) and inrange(pos[1],target[1]):
		return maxh
	else:
		return None


def still_possible(pos, vx, vy, target):
	# return False if inrange to stop the while loop
	if inrange(pos[0],target[0]) and inrange(pos[1],target[1]):
		return False

	if pos[1]>min(target[1]) or vy>0:
		if vx<0:
			return pos[0] >= min(target[0])
		elif vx>0:
			return  pos[0] <= max(target[0])
		else:
			return inrange(pos[0], target[0])
	else:
		return False


def inrange(x, r):
	return x >= r[0] and x <= r[1]


if __name__ == "__main__":
	x, y = load('./day17-input.txt')
	
	hs, vels = naive_search([x,y])

	print('Maximum y position reached:', max(hs))
	print('Number of distinct velocity values that reach target:', len(hs))