def load(txt):
	with open(txt) as file:
		line = file.readline()

	return line.rstrip()

def hex_to_bin(x):
	binary = ''
	for char in x:
		binary += bin(int(char,18))[2:].zfill(4)

	return binary


def parse_literal(x):
	i = 0
	n = ''
	while x[i] == '1':
		n += x[i+1:i+5]
		i += 5
	n += x[i+1:i+5]
	i += 5
	return int(n,2), i


def parse_package(x, tree, start=0):
	version  = int(x[start:start+3],2)
	typeid = int(x[start+3:start+6],2)

	tree['version']  = version
	tree['typeid']   = typeid
	tree['children'] = []

	if typeid != 4:
		len_id = x[start+6]

		if len_id == '0':
			# N BITS IN SUBPACKETS
			nbits = int(x[start+7:start+22],2)
			curr = start+22

			while curr < start+22+nbits:
				tree['children'].append({})
				curr = parse_package(x, tree['children'][-1], start=curr)

			return curr

		else:
			# N SUBPACKETS
			nsub = int(x[start+7:start+18],2)
			curr = start+18

			for _ in range(nsub):
				tree['children'].append({})
				curr = parse_package(x, tree['children'][-1], start=curr)

			return curr

	else:
		content, i = parse_literal(x[start+6:])

		tree['value'] = content

		return start+6+i


class BITS:

	def __init__(self, communication):
		self.communication = communication
		self.binary = hex_to_bin(communication)

		self.tree = {}
		parse_package(self.binary, self.tree)

	def version_sum(self):

		def _sum(tree, n):
			n += tree['version']
			for x in tree['children']:
				n = _sum(x,n)
			return n

		return _sum(self.tree, 0)

	def compute(self):

		def _compute(tree):
			if tree['typeid'] == 4:
				return tree['value']
			elif tree['typeid'] == 0:
				return sum([_compute(x) for x in tree['children']])
			elif tree['typeid'] == 1:
				def prod(x):
					if len(x)<1: return 1
					else: return x[0]*prod(x[1:])
				return prod([_compute(x) for x in tree['children']])
			elif tree['typeid'] == 2:
				return min([_compute(x) for x in tree['children']])
			elif tree['typeid'] == 3:
				return max([_compute(x) for x in tree['children']])
			elif tree['typeid'] == 5:
				return int(_compute(tree['children'][0]) > _compute(tree['children'][1]))
			elif tree['typeid'] == 6:
				return int(_compute(tree['children'][0]) < _compute(tree['children'][1]))
			elif tree['typeid'] == 7:
				return int(_compute(tree['children'][0]) == _compute(tree['children'][1]))

		return _compute(self.tree)


if __name__ == "__main__":
	comm = load('./day16-input.txt')
	
	bits = BITS(comm)

	print('Version sum:', bits.version_sum())
	
	print('Result:', bits.compute())

	