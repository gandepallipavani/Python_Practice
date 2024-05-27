#Program to determine grade of a student based on percentage 

percent= int(input("Enter percentage of student: "))

if (percent>100):
	print("Enter below 100")

elif (percent>=90):
	print("A")
elif (percent>=80):
	print("B")
elif (percent>=70):
	print("B-")
elif (percent>=60):
	print("C")
elif (percent>=50):
	print("C-")
elif (percent>=40):
	print("D")
else:
	print("Fail")