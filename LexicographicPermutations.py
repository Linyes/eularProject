import math

limit = 1000000

digits = [0,1,2,3,4,5,6,7,8,9]

count = 0

result = ""

for rest in range(9,-1,-1):
	num = math.factorial(rest)
	for digit in digits:
		if count + num < limit:
			count += num
			continue
		else:
			result+=str(digit)
			digits.remove(digit)
			break

print result
