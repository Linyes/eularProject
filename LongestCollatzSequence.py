size = 1000000
sieve = [0] * size

def Collatz(num):
	n = num
	count = 1
	while n != 1:
		if n <= 1000000 and sieve[n-1] != 0:
			sieve[num-1] = sieve[n-1] + count
			return sieve[num-1]
		if n % 2 == 0:
			n /= 2
		else:
			n = 3*n+1
		count+=1

	return count


for i in range(size):
	if sieve[i] == 0:
		sieve[i] = Collatz(i+1)

print sieve.index(max(sieve))+1


