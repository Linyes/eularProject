f=open('problem13.txt','r')

input=map(int,f.read().splitlines())
sum=repr(sum(input))
print sum[0:10]
