# Program to calculate the electricity bill 

units = int(input("No.Of Units: "))
if (units <= 100):
	print("Bill is ", units * 10)
	
elif (units <= 200):
	print("Bill is ", ((100 * 10) + (units - 100) * 15))
	
elif (units <= 300):
	print("Bill is ", ((100 * 10) + (100 * 15) + (units - 200) * 20)) 
	
elif (units > 300):
	print("Bill is ", ((100 * 10) + (100 * 15) + (100 * 20) + (units - 300) * 25))
	

