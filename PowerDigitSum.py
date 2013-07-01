target = pow(2, 1000)
sum = 0
while target:
	digit = target % 10
	target /= 10
	sum += digit

print sum
