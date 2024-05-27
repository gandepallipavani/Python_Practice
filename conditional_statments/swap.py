a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
print("A = {} and B = {}".format(a, b))
a = a + b
b = a - b
a = a - b
print("After swap A = {} and B = {}".format(a, b))
c=5
d=7
c,d=d,c
print("c={} d={}".format(c,d))