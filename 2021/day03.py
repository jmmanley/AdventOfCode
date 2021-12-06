def load(txt):
	with open(txt) as file:
		return file.readlines()

def more_ones(logs, bit):
	return sum([int(x[bit]) for x in logs]) >= len(logs)/2

if __name__ == "__main__":
	logs = load('./day03-input.txt')

	logs_o2  = logs.copy() # logs still potentially in running for o2 generator
	logs_co2 = logs.copy() # logs still potentially in running for co2 scrubber

	n_bits = len(logs[0][:-1])
	n_logs = len(logs)

	gamma_rate   = ''
	epsilon_rate = ''

	for i in range(n_bits):
		# count number of ones in i-th bit

		if more_ones(logs, i):
			# MORE ONES
			gamma_rate   += '1'
			epsilon_rate += '0'
		else:
			# MORE ZEROS
			gamma_rate   += '0'
			epsilon_rate += '1'

		if len(logs_o2) > 1:
			if more_ones(logs_o2, i):
				logs_o2 = [x for x in logs_o2 if x[i] == '1']
			else:
				logs_o2 = [x for x in logs_o2 if x[i] == '0']

		if len(logs_co2) > 1:
			if more_ones(logs_co2, i):
				logs_co2 = [x for x in logs_co2 if x[i] == '0']
			else:
				logs_co2 = [x for x in logs_co2 if x[i] == '1']


	# convert decimal to binary and multiply
	power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

	print('submarine power consumption:', power_consumption)

	o2_generator = int(logs_o2[0], 2)
	co2_scrubber = int(logs_co2[0], 2)

	life_support_rating = o2_generator * co2_scrubber

	print('submarine life support rating:', life_support_rating)
