def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	dots = [[int(n) for n in x.rstrip().split(',')] for x in lines if x != '\n' and x[0] != 'f']

	folds = [x.rstrip() for x in lines if x[0] == 'f']

	return dots, folds

class Paper:

	def __init__(self, dots):
		sizex = max([x[0] for x in dots])+1
		sizey = max([x[1] for x in dots])+1

		self.paper = [[False for _ in range(sizey)] for _ in range(sizex)]

		for dot in dots:
			self.paper[dot[0]][dot[1]] = True

	def fold(self, instruction):
		xy,n = instruction.split('=')
		xy = xy[-1]
		n  = int(n)

		if xy == 'x':
			newpaper = self.paper[:n]
			for i in range(len(newpaper)):
				for j in range(len(newpaper[0])):
					newpaper[n-i-1][j] = self.paper[n-i-1][j] or self.paper[n+i+1][j]
			self.paper = newpaper
		else:
			newpaper = [x[:n] for x in self.paper]
			for i in range(len(newpaper)):
				for j in range(len(newpaper[0])):
					newpaper[i][n-j-1] = self.paper[i][n-j-1] or self.paper[i][n+j+1]

			self.paper = newpaper

	def n_dots(self):
		return sum([x for row in self.paper for x in row])

	def print(self):
		img = [['**' if paper.paper[j][i] else '  ' for j in range(len(paper.paper))] for i in range(len(paper.paper[0]))]
		for x in img:
			print(''.join(x))


if __name__ == "__main__":
	dots, folds = load('./day13-input.txt')
	
	paper = Paper(dots)

	paper.fold(folds[0])

	print('Number of dots after first fold:', paper.n_dots())

	for fold in folds[1:]:
		paper.fold(fold)


	print('The code is:')
	paper.print()