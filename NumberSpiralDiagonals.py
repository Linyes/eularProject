sum = 1
last = 1
for i in range(3,1003,2):
	last += 2*i+2*(i-2)
	sum += last
	sum += last-i+1
	sum += last-2*(i-1)
	sum += last-3*(i-1)

print sum
