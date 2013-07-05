def value(s):
	sum = 0
	base = 64
	for i in range(len(s)):
		sum += (ord(s[i])-base)

	return sum

f=open('names.txt','r')
line = f.readline()
names = line.replace('\"','').split(',')
names.sort()

ret = 0
for i in range(len(names)):
	ret += (i+1)*value(names[i])

print ret

