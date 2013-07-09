import math
import time

start = time.time()

primes = [2,3,5,7]
def isPrime(n):
	upperlimit = int(math.sqrt(n))
	for i in primes:
		if i > upperlimit:
			break
		if n % i == 0:
			return False
	
	return True

for i in range(12, 1000000,6):
	if isPrime(i-1):
		primes.append(i-1)
	if isPrime(i+1):
		primes.append(i+1)

def rotateLeft(n):
	s = str(n)
	return int(s[1:]+s[0])

primes = set(primes)

nums = 0
target = set()
for i in primes:
	if i in target:
		continue
	digits = map(int,str(i))
	if 0 in digits:
		continue

	num = i
	size = int(math.ceil(math.log10(i)))
	tmp = set()
	for j in range(size):
		tmp.add(num)
		num = rotateLeft(num)
	
	if tmp.issubset(primes):
		nums += size
		for x in tmp:
			target.add(x)
#print sorted(target)	
print len(target)
print time.time()-start


