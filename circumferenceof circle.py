# to calculate the circumference of circle
import math
radius = float(input ("Enter the radius of circle: "))
math.pi
C = 2 * math.pi * radius
print(f"The circumference of circle is : {C}")
print(f"The circumference of circle is : {round(C,2)}cm")
#to find area of circle
import math
radius = float(input("Enter the radius of circle: "))
Area = (math.pi * pow(radius,2))
print(f"The area of circle is : {round(Area,2)}cm^2")
#to find hypotenuse of a right angled triangle
import math 
P = float(input("Enter the length of perpendicular: "))
B = float(input("Enter the length of base: "))
H = math.sqrt((pow(P,2) + pow(B,2)))
print(f"The Hypotenuse of a right angled triangle is :{H} ")