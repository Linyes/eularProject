# c should less than 500
for c in range(499, 1, -1):
	sum = 1000 - c
	for b in range(sum-1,int(sum/2),-1):
		a = sum - b
		left = pow(a,2)+pow(b,2)
		right = pow(c,2)
		if right == left:
			print a*b*c
