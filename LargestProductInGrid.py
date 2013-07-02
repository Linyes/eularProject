f = open('problem11.txt', 'r')
input = []
length = 4

for line in f:
	input.append(map(int,line.split()))

m = len(input)
n = len(input[0])
max = 0
#up-down direction
for i in range(n):
	product = input[0][i]*input[1][i]*input[2][i]*input[3][i]
	if product > max:
		max = product

	for j in range(4,m):
		if input[j-4][i] != 0:
			product /= input[j-4][i]
		else:
			product = input[j-3][i]*input[j-2][i]*input[j-1][i]

		product *= input[j][i]

		if product > max:
			max = product
#left-right direction
for i in range(n):
	product = input[i][0]*input[i][1]*input[i][2]*input[i][3]
	if product > max:
		max = product

	for j in range(4,m):
		if input[i][j-4] != 0:
			product /= input[i][j-4]
		else:
			product = input[i][j-3]*input[i][j-2]*input[i][j-1]

		product *= input[i][j]

		if product > max:
			max = product

#diagonally direction
for i in range(m-length+1):
	for j in range(n-length+1):
		product = input[i][j]*input[i+1][j+1]*input[i+2][j+2]*input[i+3][j+3]
		if product > max:
			max = product

#right-top to left-bottom
for i in range(m-length+1):
	for j in range(3,n):
		product = input[i][j]*input[i+1][j-1]*input[i+2][j-2]*input[i+3][j-3]
		if product > max:
			max = product
print max

