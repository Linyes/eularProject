length = 1
n_2 = 1
n_1 = 1
count = 2
while length < 1000:
	count += 1
	n = n_1 + n_2
	length = len(str(n))
	n_2 = n_1
	n_1 = n

print count
