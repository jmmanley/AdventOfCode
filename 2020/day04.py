def parse_passport_batch(file):
	passports = []
	with open(file,'r') as input:
		line = input.readline()
		curr = dict()
		while line:
			if line == "\n":
				passports.append(curr)
				curr = dict()
			else:
				for pair in line.split():
					kv = pair.split(":")
					curr[kv[0]] = kv[1]
			
			line = input.readline()
		
		passports.append(curr)	

	return passports

def is_valid_part1(passport, required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']):
	keys = passport.keys()
	for key in required:
		if key not in keys: return 0
	
	return 1

def is_valid_part2(passport):
	if is_valid_part1(passport):
		try:
			if int(passport['byr']) < 1920 or int(passport['byr']) > 2002: return 0
			
			if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020: return 0
			
			if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030: return 0

			hgt_unit = passport['hgt'][-2:]
			hgt_num  = int(passport['hgt'][:-2])
			if hgt_unit == 'in':
				if hgt_num < 59 or hgt_num > 76: return 0
			elif hgt_unit == 'cm':
				if hgt_num < 150 or hgt_num > 193: return 0
			else: return 0
			
			if passport['hcl'][0] != '#': return 0
			
			for x in passport['hcl'][1:]:
				try:
					int(x)
				except:
					if x not in ['a','b','c','d','e','f']: return 0

			if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				return 0
			
			test = int(passport['pid'])
			if len(passport['pid']) != 9: return 0

		except:
			return 0
		return 1
	else: return 0

if __name__ == "__main__":
	passports = parse_passport_batch('day04-input.txt')
	
	print('part 1, count number of valid passports:')
	print(sum([is_valid_part1(passport) for passport in passports]))	
	
	print('part 2, count number of passports with valid data:')
	print(sum([is_valid_part2(passport) for passport in passports]))
