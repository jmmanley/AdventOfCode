def load(txt):
	with open(txt) as file:
		return file.readlines()

if __name__ == "__main__":
	logs = load('./day03-input.txt')

	n_bits = len(logs[0][:-1])
	n_logs = len(logs)

	gamma_rate   = ''
	epsilon_rate = ''

	for i in range(n_bits):
		# count number of ones in i-th bit
		n_ones = sum([int(x[i]) for x in logs])

		if n_ones > n_logs/2:
			# MORE ONES
			gamma_rate   += '1'
			epsilon_rate += '0'
		else:
			# MORE ZEROS
			gamma_rate   += '0'
			epsilon_rate += '1'

	# convert decimal to binary and multiply
	power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

	print('submarine power consumption:', power_consumption)
