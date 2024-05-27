#Programe to determine the type of triangle based on the sides 

print("Input lengths of the triangle sides: ")

x = int(input("x: "))

y = int(input("y: "))

z = int(input("z: "))


# If all sides are equal, display that it's an equilateral triangle
if x == y == z:
    print("Equilateral triangle")

# If at least two sides are equal, display that it's an isosceles triangle
elif x == y or y == z or z == x:
    print("Isosceles triangle")

# If all sides have different lengths, display that it's a scalene triangle
else:
    print("Scalene triangle") 
