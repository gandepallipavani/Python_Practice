# Python program to find the largest number among the three numbers 
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: ")) 

if (a >= b) and (a >= c):
	print("{} is the largest".format(a), "of", a,b,c)
 
elif (b >= a) and (b >= c): 
	print("{} is the largest".format(b), "of", a,b,c)

else: 
	print("{} is the largest".format(c), "of", a,b,c)

