n=int(input("Enter a num.: "))
fact=1
for i in range(n,0,-1):
	fact*=i
print("Factorial of ",n," is ",fact)