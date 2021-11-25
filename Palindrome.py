s=input('enter your string')
n=len(s)
p=''
for i in range(n-1,-1,-1):
    p=p+s[i]
if p==s:
    print(s,'is a palindrome')
else:
    print(s,'is not a palindrome')
