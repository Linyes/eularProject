import math
from math import factorial
import time

def getDigits(n):
	return map(int, list(str(n)))

start = time.time()
result = 0

for i in range(3,100000):
	if sum(map(factorial, getDigits(i))) == i:
			result += i

print result
print "Run Time = " + str(time.time() - start)
