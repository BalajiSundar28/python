n=int(input('enter number'))
r=0
sum=0
while n>0:
	r=n%10
	sum=sum*10+r
	n=n//10
print('reverse of the given number is',sum)
