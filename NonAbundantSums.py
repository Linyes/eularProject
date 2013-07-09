import math
import itertools

abundant=[]

for i in range(12,28124):
	limit = int(math.sqrt(i))
	divisors = [1]
	for x in range(2,limit+1):
		if i % x == 0:
			divisors.append(x)
			if x != math.sqrt(i):
				divisors.append(i/x)
	if sum(divisors) > i:
		abundant.append(i)

not_sum_of_abundant = range(28124)

for i in abundant:
	for j in abundant:
		sum = i + j
		if sum > 28123:
			break
		elif sum in not_sum_of_abundant:
			not_sum_of_abundant.remove(sum)

print sum(not_sum_of_abundant)
		
