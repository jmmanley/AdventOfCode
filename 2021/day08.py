def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	signals = [line.split('|')[0] for line in lines]
	signals = [signal.split(' ')[:-1] for signal in signals]

	outputs = [line.split('|')[1][1:] for line in lines]
	outputs = [output.rstrip().split(' ') for output in outputs]

	return signals, outputs

def count_specific_lengths(inputs, lengths):
	return sum([len(x) in lengths for x in inputs])

def find_mapping(signals):
	# APPROACH HERE IS BASED ON VISUALLY INSPECTING THE DIFFERENCES BETWEEN LETTERS

	mapping = [[] for _ in range(10)]

	# FIRST: FIND UNIQUE N SEGMENTS
	mapping[1] = [x for x in signals if len(x)==2][0]
	mapping[4] = [x for x in signals if len(x)==4][0]
	mapping[7] = [x for x in signals if len(x)==3][0]
	mapping[8] = [x for x in signals if len(x)==7][0]

	# SOME SEGMENTS WE NOW KNOW
	a = [i for i in mapping[7] if i not in mapping[1]][0]
	eg = [i for i in mapping[8] if i not in mapping[4]+a]

	# FIND ALL WITH LENGTH 6
	len6 = [x for x in signals if len(x)==6]
	m60 = [x for x in len6 if all([i in x for i in eg])]
	mapping[0] = [x for x in m60 if all(i in x for i in mapping[1])][0]
	mapping[9] = [x for x in len6 if x not in m60][0]
	mapping[6] = [x for x in m60 if x != mapping[0]][0]

	# SOME MORE SEGMENTS WE NOW KNOW
	e = [i for i in eg if i not in mapping[9]][0]

	# FIND ALL WITH LENGTH 5
	len5 = [x for x in signals if len(x)==5]
	mapping[2] = [x for x in len5 if e in x][0]
	len5left = [x for x in len5 if x != mapping[2]]
	mapping[3] = [x for x in len5left if all([i in x for i in mapping[1]])][0]
	mapping[5] = [x for x in len5left if x != mapping[3]][0]

	dict_mapping = dict()

	for i in range(len(mapping)):
		dict_mapping[mapping[i]] = i

	return dict_mapping

def solve(signal, output):

	# sort all strings to ensure order is consistent
	signal = [''.join(sorted(x)) for x in signal]
	output = [''.join(sorted(x)) for x in output]

	mapping = find_mapping(signal)

	return int(''.join([str(mapping[x]) for x in output]))


if __name__ == "__main__":
	signals, outputs = load('./day08-input.txt')

	# Part 1: count the number of times 1, 4, 7, or 8 appear.
	# These each have a unique number of segments: 2, 4, 3, and 7, respectively
	unique_n_segments = [2, 4, 3, 7]

	n_1478 = sum([count_specific_lengths(output, unique_n_segments) for output in outputs])

	print('Number of 1s, 4s, 7s and 8s in output:', n_1478)

	total_sum = sum([solve(signals[i], outputs[i]) for i in range(len(signals))])

	print('Sum of all outputs:', total_sum)
	