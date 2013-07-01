import math

count = 1
sum = 0

while True:
	sum += count
	num = sum
	numDiv = 0
	for i in range(int(math.sqrt(sum))):
		if sum%(i+1) == 0:
			if i+1 == int(math.sqrt(sum)):
				numDiv += 1
			else:
				numDiv+=2
	if numDiv >= 500:
		break
	count += 1
	print numDiv
print sum
