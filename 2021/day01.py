def load(txt):
	with open(txt, 'r') as file:
		lines = file.readlines()

	return [int(x) for x in lines]

def diff(x):
	### PROBLEM: MAXIMUM RECURSION DEPTH EXCEEDED
	if len(x)<2:
		return []
	else:
		return [x[1]-x[0]] + diff(x[1:])

if __name__ == "__main__":
	data = load('./day01-input.txt')

	# Manually iterate and count increases

	n_increasing = 0
	for i in range(1,len(data)):
		if data[i]>data[i-1]:
			n_increasing += 1
	
	print('raw number increasing:', n_increasing)

	# Manually iterate, calculate sliding window, and count increases
	k = 3 # length of sliding window

	prev_sum = sum(data[:k])
	n_increasing = 0
	for i in range(1,len(data)-k+1):
		curr_sum = sum(data[i:i+k])
		if curr_sum > prev_sum:
			n_increasing += 1
		prev_sum = curr_sum

	print('sliding window k='+str(k),'number increasing:', n_increasing)