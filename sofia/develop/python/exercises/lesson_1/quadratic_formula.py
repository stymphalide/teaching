import math

a = input("Your value for 'a': ")
b = input("Your value for 'b': ")
c = input("Your value for 'c': ")

a = float(a)
b = float(b)
c = float(c)

discrimnant = b**2 -4*a*c

if discrimnant <0:
	print("discrimnant is negative!!!")
else:
	x1 = (-b + math.sqrt(discrimnant))/(2*a)
	x2 = (-b - math.sqrt(discrimnant))/(2*a)


	print(a,b,c)
	print(x1,x2)

