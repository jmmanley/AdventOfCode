from utils import diff

def binary2int(bin):
	n = 2 ** len(bin)
	
	if n == 1: return 0
	
	if bin[0]: return binary2int(bin[1:]) + int(n/2)
	else:      return binary2int(bin[1:])

def seatID(bin):
	row_bin = [x == 'B' for x in bin[:7]]
	row = binary2int(row_bin)
	
	col_bin = [x == 'R' for x in bin[7:10]]
	col = binary2int(col_bin)
	
	return row*8 + col

def findSeat(ids):
	# seat is the only one missing in list, but list
	idx = diff(ids).index(2)
	return ids[idx]+1

if __name__ == "__main__":
	input = open('day05-input.txt', 'r')
	lines = input.readlines()
	
	ids = sorted([seatID(line) for line in lines])

	print('part 1, highest seat ID:')
	print(ids[-1])
	
	print('part 2, find my seat ID:')
	print(findSeat(ids))
