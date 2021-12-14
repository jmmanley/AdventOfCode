def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	return lines

class Circuit:

	def __init__(self, instructions=[]):
		self.wires = dict()
		self.wires['1'] = 1

		try_again = instructions

		while len(try_again) > 0:
			# The order of the instructions is important!
			# In this brute force approach, just keep trying all of the instructions
			# until they are all applied!
			todo = try_again
			try_again = []	

			for i in todo:
				try:
					self.add(i)
				except:
					try_again.append(i)

	def add(self, instruction):
		pieces = instruction.split('->')

		output = pieces[1].strip(' ').rstrip()

		inputs = [x.strip(' ').rstrip() for x in pieces[0].split(' ') if x != '']

		if len(inputs) == 1:
			# SIGNAL
			try:
				self.wires[output] = int(inputs[0])
			except:
				self.wires[output] = self.wires[inputs[0]]
		elif len(inputs) == 2:
			# NOT
			self.wires[output] = ~self.wires[inputs[1]]
		elif len(inputs) == 3:
			if inputs[1] == 'AND':
				# AND
				# if inputs[0] == '1':
				# 	self.wires[output] = 1 & self.wires[inputs[2]]
				self.wires[output] = self.wires[inputs[0]] & self.wires[inputs[2]]
			elif inputs[1] == 'OR':
				# OR
				self.wires[output] = self.wires[inputs[0]] | self.wires[inputs[2]]
			elif inputs[1] == 'LSHIFT':
				# LSHIFT
				self.wires[output] = self.wires[inputs[0]] << int(inputs[2])
			elif inputs[1] == 'RSHIFT':
				# RSHIFT
				self.wires[output] = self.wires[inputs[0]] >> int(inputs[2])


if __name__ == "__main__":
	instructions = load('./day07-input.txt')

	circuit = Circuit(instructions)

	print('Signal to wire a:', circuit.wires['a'])

	instructions_override_b = [x for x in instructions if x[-5:-1] != '-> b']
	instructions_override_b.append(str(circuit.wires['a']) + ' -> b')

	circuit_override_b = Circuit(instructions_override_b)

	print('Signal to wire a after overriding b:', circuit_override_b.wires['a'])