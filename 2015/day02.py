def load(txt):
	with open(txt) as file:
		lines = file.readlines()

	dims = [x.split('x') for x in lines]
	dims = [[int(x) for x in dim] for dim in dims]

	return dims

def surface_area(dim):
	return 2*(dim[0]*dim[1] + dim[1]*dim[2] + dim[0]*dim[2])

def slack(dim):
	return min(dim[0]*dim[1], dim[1]*dim[2], dim[0]*dim[2])

def wrapping_paper(dim):
	return surface_area(dim) + slack(dim)

def volume(dim):
	return dim[0]*dim[1]*dim[2]

def smallest_perimeter(dim):
	return 2*min(dim[0]+dim[1], dim[1]+dim[2], dim[0]+dim[2])

def ribbon(dim):
	return smallest_perimeter(dim) + volume(dim)

if __name__ == "__main__":
	dims = load('./day02-input.txt')

	total_wrapping_paper = sum([wrapping_paper(dim) for dim in dims])

	print('Square feet of wrapping paper needed:', total_wrapping_paper)

	total_ribbon = sum([ribbon(dim) for dim in dims])

	print('Feet of ribbon needed:', total_ribbon)