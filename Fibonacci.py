n=int(input('enter n value'))
f=f1=0
f2=1
while f<n:
	f=f1+f2
	f1=f2
	f2=f
	print(f)
