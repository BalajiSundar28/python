n=int(input('enter number'))
i=2
a=0
while i<=n-1:
	if n%i==0:
		print(n,'is not a composite number')
		break
	i=i+1
if i==n:
	print(n,'is a prime number')
