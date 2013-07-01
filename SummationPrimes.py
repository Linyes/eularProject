import math
import time

count = 12
sum = 17
max = 2000000
def isPrime(n):
	if n%2==0 or n % 5 == 0 or n%3==0 or n%7==0:
		return False
	top = math.sqrt(n)
	ne = 5
	while ne <= top:
		if n % ne ==0:
			return False
		if n %(ne+2) == 0:
			return False
		ne += 6

	return True

start_time = time.time()
for i in range(11,max+1,2):
	if isPrime(i):
		sum += i
#		print i
print "total time", time.time()-start_time
#print isPrime(121)
print sum
