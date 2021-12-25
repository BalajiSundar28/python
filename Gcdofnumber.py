a=int(input('enter 1st number'))
b=int(input('enter 2nd number'))
if a<b:
	smaller=a
elif b<a:
	smaller=b
else:
	print('do not give 2 equal numbers')
for i in range(1,smaller+1):
	if a%i==0 and b%i==0:
		gcd=i
print('greatest common devisor is',gcd)
