def load(txt):
	with open(txt) as file:
		line = file.readline()

	return line

import hashlib

def hex_has_prefix(input, prefix):
	md5 = hashlib.md5(input)

	if md5.hexdigest()[:len(prefix)] == prefix:
		return True
	else:
		return False

if __name__ == "__main__":
	puzzle = load('./day04-input.txt')

	i = 0
	while not hex_has_prefix((puzzle+str(i)).encode(), '00000'):
		i += 1

	print('Lowest number that gives 5 zeros prefix:', i)

	i = 0
	while not hex_has_prefix((puzzle+str(i)).encode(), '000000'):
		i += 1

	print('Lowest number that gives 6 zeros prefix:', i)