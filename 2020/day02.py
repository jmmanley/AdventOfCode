def is_valid_password_part1(password, policy):
	mi = int(policy.split('-')[0])
	ma = int(policy.split('-')[1].split(' ')[0])
	let = policy.split(' ')[1]
	
	count = 0

	for x in password:
		if x == let:
			count = count + 1
			if count > ma: return 0
	
	if count < mi: return 0
	else:          return 1


def is_valid_password_part2(password, policy):
	i1 = int(policy.split('-')[0])
	i2 = int(policy.split('-')[1].split(' ')[0])
	let = policy.split(' ')[1]

	return (password[i1-1] == let) ^ (password[i2-1] == let)


if __name__ == "__main__":
	input = open('day02-input.txt', 'r')
	lines = input.readlines()
	
	def parse_input(line):
		parts = line.split(":")
		return parts[1][1:], parts[0]

	print('part 1, number of valid passwords:')
	print(sum([is_valid_password_part1(*parse_input(line)) for line in lines]))
	
	print('part 2, number of valid passwords:')
	print(sum([is_valid_password_part2(*parse_input(line)) for line in lines]))
