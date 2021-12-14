def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	start = lines[0].rstrip()
	rules = [x.rstrip() for x in lines[2:]]

	return start, rules

class Polymer:

	def __init__(self, start, rules):
		self.polymer = start

		self.rules = dict()

		for rule in rules:
			rule = [rule[0], rule[1], rule[-1]]
			
			if rule[0] not in self.rules.keys():
				self.rules[rule[0]] = dict()

			self.rules[rule[0]][rule[1]] = rule[2]

	def polymerize(self):
		newpolymer = self.polymer[0]

		for i in range(len(self.polymer)-1):
			newpolymer += self.rules[self.polymer[i]][self.polymer[i+1]]
			newpolymer += self.polymer[i+1]

		self.polymer = newpolymer

	def count_elements(self):
		counts = dict()

		for x in self.rules.keys():
			counts[x] = sum([a==x for a in self.polymer])

		return counts

class PolymerCounts:

	def __init__(self, start, rules):
		self.polymer = start

		self.rules = dict()
		self.pairs = dict()
		self.counts = dict()
		# It is too expensive to count letters in recursive fashion.
		# Only need to keep track of the PAIRS of letters and their counts!

		for rule in rules:
			rule = [rule[0], rule[1], rule[-1]]
			
			if rule[0] not in self.rules.keys():
				self.rules[rule[0]] = dict()
				self.counts[rule[0]] = 0
			if rule[0]+rule[1] not in self.pairs.keys():
				self.pairs[rule[0]+rule[1]] = 0

			self.rules[rule[0]][rule[1]] = rule[2]

		for i in range(len(start)-1):
			self.pairs[start[i:i+2]] += 1

		for i in range(len(start)):
			self.counts[start[i]] += 1

	def polymerize(self):
		
		for key, val in self.pairs.copy().items():
			newchar = self.rules[key[0]][key[1]]

			self.pairs[key] -= val
			self.pairs[key[0]+newchar] += val
			self.pairs[newchar+key[1]] += val

			self.counts[newchar] += val

	def count_elements(self):
		return self.counts

if __name__ == "__main__":
	start, rules = load('./day14-input.txt')

	p = Polymer(start, rules)

	for _ in range(10): p.polymerize()

	counts = p.count_elements()
	print('Difference between quantitites of most and least common elements after 10 steps:', max(counts.values())-min(counts.values()))

	p = PolymerCounts(start, rules)
	for _ in range(40): p.polymerize()

	counts = p.count_elements()
	print('Difference between quantitites of most and least common elements after 40 steps:', max(counts.values())-min(counts.values()))
