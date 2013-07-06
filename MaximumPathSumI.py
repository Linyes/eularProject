tree = []

f=open('67.txt','r')

#tree[a][b] means row a and colum b
tree = [map(int,line.strip().split()) for line in f]

depth = len(tree)

#cache the maximum path sum at given position
cache = []
for line in tree:
	if line == tree[depth-1]:
		cache.append(line)
	else:
		cache.append([-1]*len(line))

def maxpath(a,b):
	if cache[a][b] != -1:
		return cache[a][b]

	left = cache[a+1][b]
	if left == -1:
		left = maxpath(a+1,b)
	
	right = cache[a+1][b+1]
	if right == -1:
		right = maxpath(a+1,b+1)
	
	cache[a][b] = max(left,right)+tree[a][b]

	return cache[a][b]

print maxpath(0,0)

