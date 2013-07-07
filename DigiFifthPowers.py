import itertools

power = 5
digits=[0,1,2,3,4,5,6,7,8,9]
powers=[power]*10

powerlist = [x for x in itertools.imap(pow,digits,powers)]

sum = 0

for i in range(10,999999):
	number = [int(x) for x in str(i)]
	checknum = 0

	for x in number:
		checknum += powerlist[x]
		if checknum > i:
			break
		
	
	if checknum == i:
		print checknum,i	
		sum += i

print sum
