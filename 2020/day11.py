def up(idx): return (idx[0]+1, idx[1])
def down(idx): return (idx[0]-1, idx[1])
def left(idx): return (idx[0], idx[1]-1)
def right(idx): return (idx[0], idx[1]+1)
def urdiag(idx): return (idx[0]+1, idx[1]+1)
def uldiag(idx): return (idx[0]+1, idx[1]-1)
def drdiag(idx): return (idx[0]-1, idx[1]+1)
def dldiag(idx): return (idx[0]-1, idx[1]-1)

class WaitingRoom:
	def __init__(self, input):
		with open(input) as f:
			self.grid = f.readlines()
		self.grid = [line.strip().rstrip('\n') for line in self.grid]

		self.m = len(self.grid)
		self.n = len(self.grid[0])

		self.isStable = False
	
	def isOccupied(self, idx):
		if idx[0]<0 or idx[0]>=self.m or idx[1]<0 or idx[1]>=self.n: return False
		
		return self.grid[idx[0]][idx[1]] == '#'	
	
	def isEmpty(self, idx):
		if idx[0]<0 or idx[0]>=self.m or idx[1]<0 or idx[1]>=self.n: return False

		return self.grid[idx[0]][idx[1]] == 'L'
	
	def isCramped(self, idx):
		count = 0

		for curr in [up(idx),down(idx),left(idx),right(idx),urdiag(idx),uldiag(idx),drdiag(idx),dldiag(idx)]:
			if self.isOccupied(curr):
				count += 1
		
		return count > 3
	
	def isSpacious(self, idx):
		count = 0

		for curr in [up(idx),down(idx),left(idx),right(idx),urdiag(idx),uldiag(idx),drdiag(idx),dldiag(idx)]:
			if self.isOccupied(curr): return False

		return True
	
	def update(self):
		changed = False
		newgrid = self.grid.copy()
		
		for i in range(self.m):
			for j in range(self.n):
				if self.isEmpty((i,j)) and self.isSpacious((i,j)): 
					newgrid[i] = newgrid[i][:j] + '#' + newgrid[i][j+1:]
					changed = True

				if self.isOccupied((i,j)) and self.isCramped((i,j)):
					newgrid[i] = newgrid[i][:j] + 'L' + newgrid[i][j+1:]
					changed = True
		
		self.grid = newgrid	
		if not changed: self.isStable = True
	
	def nOccupied(self):
		count = 0
		for i in range(self.m):
			for j in range(self.n):
				if self.isOccupied((i,j)): count += 1
		return count

if __name__ == "__main__":
	room = WaitingRoom('day11-input.txt')
	print(room.grid)
	while not room.isStable:
		room.update()
	
	print('part 1, number of occupied seats when stable:')
	print(room.nOccupied())
