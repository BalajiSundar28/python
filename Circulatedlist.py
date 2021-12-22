n=int(input('enter number of values to be imported in the list'))
list1=[]
for i in range(0,n):
	a=int(input('enter list element'))
	list1.append(a)
print('list to be circulated=',list1)
for i in range(0,n):
	result=list1[i:]+list1[:i]
	print(result)
