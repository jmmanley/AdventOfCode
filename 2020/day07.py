class Rules:
	def __init__(self, input):
		self.bags = dict()
		
		with open(input, 'r') as f:
			lines = f.readlines()
		
		for line in lines:
			parts = line.split(' bags contain ')
			bag = parts[0]
			
			innards = parts[1].split(', ')
			
			self.bags[bag] = dict()
			
			for x in innards:
				try:
					parts = x.split(' ')
					n = int(parts[0])
				
					color = ' '.join(parts[1:3])
					self.bags[bag][color] = n
				except:
					continue
	
	def eventually_contains(self, bag, goal):
		keys = self.bags[bag].keys()
		
		if goal in keys: return True
		else:
			for x in keys:
				if self.eventually_contains(x, goal): return True
		
		return False				
	
	def number_of_bags_inside(self, bag):
		count = 0		
		
		for x in self.bags[bag].keys():
			count += self.bags[bag][x]*(self.number_of_bags_inside(x) +1)

		return count
			
		
if __name__ == "__main__":
	rules = Rules('day07-input.txt')
	count = 0
	for bag in rules.bags.keys():
		if rules.eventually_contains(bag, 'shiny gold'): count += 1
	
	print('part 1, number of bags that can contain a shiny gold bag:')
	print(count)
	
	print('part 2, number of bags inside a shiny gold bag:')
	print(rules.number_of_bags_inside('shiny gold'))
