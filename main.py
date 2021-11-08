n=input("Enter the number")
nu=n
sum=0
while(n>0):
	r=n%10
	sum=(sum*10)+r
	n=n/10
if(sum==nu):
	print("palindrome")
else:
	print("not palindrome")
	