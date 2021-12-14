def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	return [x.rstrip() for x in lines]

def n_char_memory(x):
	# count the number of characters in memory!

	# remove quotes at beginning and end
	x = x[1:-1]

	n = 0
	i = 0

	while i < len(x):
		if x[i] == '\\':
			if x[i+1] == 'x':
				i += 4
			else:
				i += 2
		else:
			i += 1

		n += 1

	return n

def n_char_to_encode(x):
	# count the number of characters required to encode a string

	n = 6 # quotes at beginning and end
	i = 0

	# remove quotes at beginning and end
	x = x[1:-1]

	while i < len(x):
		if x[i] == '\\':
			if x[i+1] == 'x':
				i += 4
				n += 5
			else:
				i += 2
				n += 4
		else:
			i += 1
			n += 1

	return n

if __name__ == "__main__":
	strings = load('./day08-input.txt')

	n_chars_in_string = [len(x) for x in strings]

	n_chars_in_memory = [n_char_memory(x) for x in strings]

	print('Total characters in string minus total in memory:', sum(n_chars_in_string)-sum(n_chars_in_memory))

	n_chars_to_encode = [n_char_to_encode(x) for x in strings]

	print('Total characters to encode minus total characters originally:', sum(n_chars_to_encode)-sum(n_chars_in_string))