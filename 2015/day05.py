def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	return [line.rstrip() for line in lines]

def count_vowels(x):
	vowels = 'aeiou'
	return sum([c in vowels for c in x])

def has_repeat(x):
	for i in range(len(x)-1):
		if x[i] == x[i+1]:
			return True

	return False

def naughty_or_nice_part1(x):
	if count_vowels(x) > 2 and \
	   has_repeat(x) and \
	   'ab' not in x and 'cd' not in x and 'pq' not in x and 'xy' not in x:
	   		return True
	else:
		return False


def has_len2_repeat(x):
	for i in range(len(x)-2):
		if x[i:i+2] in x[i+2:]:
			return True

	return False

def has_repeat_with_skip(x):
	for i in range(len(x)-2):
		if x[i] == x[i+2]:
			return True

	return False

def naughty_or_nice_part2(x):
	if has_len2_repeat(x) and has_repeat_with_skip(x):
	   	return True
	else:
		return False

if __name__ == "__main__":
	strings = load('./day05-input.txt')

	is_nice_part1 = [naughty_or_nice_part1(x) for x in strings]

	print('Number of nice strings:', sum(is_nice_part1))


	is_nice_part2 = [naughty_or_nice_part2(x) for x in strings]

	print('Number of nice strings under new rules:', sum(is_nice_part2))