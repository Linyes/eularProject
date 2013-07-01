cache = {0:{0:0},1:{0:1},0:{1:1}}

def Lattice(x,y):
	if x in cache and y in cache[x]:
		return cache[x][y]
	if x == 0 or y == 0:
		ret = 1
	else:
		
		ret = Lattice(x,y-1)+Lattice(x-1,y)
	cache[x]={y:ret}
	return ret

print Lattice(20,20)
