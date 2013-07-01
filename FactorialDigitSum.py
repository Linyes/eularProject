import math

result = math.factorial(100)
sum = 0
while result:
	digit = result % 10
	result /= 10
	sum += digit

print sum
