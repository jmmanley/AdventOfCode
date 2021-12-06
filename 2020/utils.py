def prod(x,curr=1):
	if not x: return 1
	else: return x[0] * prod(x[1:])

def diff(x):
        if len(x) < 2: return []
        else: return [x[1] - x[0]] + diff(x[1:])
