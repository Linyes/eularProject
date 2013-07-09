import time

def isPalindromes(n):
	s = str(n)
	head = 0
	tail = len(s)-1

	while head < tail:
		if s[head] != s[tail]:
			return False
		head += 1
		tail -= 1
	return True

sum = 0
start = time.time()
for i in range(1, 1000001):
	b = int(bin(i)[2:])
	if isPalindromes(i) and isPalindromes(b):
		sum += i


print sum
print time.time() - start
