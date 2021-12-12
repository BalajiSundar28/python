n=int(input('enter number of data'))
i=0
l=[]
while i<n:
	a=int(input('enter list element'))
	l.append(a)
	i+=1
print(l)
min=l[0]
i=1
for i in range(len(l)):
	if l[i]<min:
		min=l[i]
		i+=1
print('minimum number in the list is',min)
