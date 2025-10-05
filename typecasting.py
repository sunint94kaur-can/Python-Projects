#Typecasting- The process of converting one data type to another is known as typecasting.
age = 25
print(type(age))
age = str(age)
type(age) 
#It gives no output if print keyword is not written along
print(type(age))
Name = "Sunint"
print(type(Name))
#input- input allows us to input data into the system.It helps us to give prompt.
name = input("What is your name? ")
print(f"Hello{name}")
# To Calculate the area of a rectangle
length = int(input ("Enter the length of rectangle: "))
width = int(input ("Enter the width of rectangle: "))
Area = length * width
print(f"The area of rectangle is : {Area}")
# Shopping Cart Program
# For this, we need 3 things- item, price and quantity
item = input("What item do you need: ? ")
Price = float(input("What is the price of that item : ?"))
Quantity = int(input("How many of that item do you want ?"))
total = Price * Quantity
print(f"Your total price is : {total}")