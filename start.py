print("Hello World")
# After this, we can write anything
if 5 > 2:
    print("Five is greater than two!")
    print("Two is smaller") #If conditional
# Assigning Values to Variables
x = 5
y = "Hello, World!"
# Looking for location
print(id(x))
print(id(y))
# Checking the type of variables
print(type(x))
print(type(y))
# Printing x and y
print(x)
print(y)
Mail = """
Multi line string
""" 
print(Mail)

d = 7.5
print(type(d))

e = int(d)
print(type(e))

f = float(e)
print(type(f))

a = 3
b = "3"

if a > int(b):
    print("a is greater")
else:
    print("b is greater")
# Python is case sensative do not forget that

myObject = 5 # Camel Case: It is not used in Python. It is used in Java and C++.
MyObject = 5 # Pascal Case: It is used while making class.
my_object = 5 # Snake Case: It is used while making variables.

#To assign multiple values to variables we can do this:
x,y,z = "Orange","Banana","Mango"
print(x,y,z)
#To assign same value to multiple variables we can do this:
x = y = z = "Orange"
print(x,y,z)
#It's called unpacking
fruits = ["apple","banana","cherry"]
a,b,c = fruits
#The t and f for True and False are capitalized.
a = True
b = False
print(a and b)
print(a or b)
print(not b)

boy_age = 19
boy_country = "Nepal"

if boy_age > 18 and boy_country == "Nepal":
    print("Boy can give licence exam in Nepal")
else:
    print("Boy cannot give licence exam in Nepal")

first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: ")) # We can do this way as well

#first_number = int(first_number): We can do this way as well
print(" Addition =", first_number + second_number)
print(" Subtraction =", first_number - second_number)
print(" Multiplication =", first_number * second_number)
print(" Division =", first_number / second_number)
print(" Modulus =", first_number % second_number)
print(" Exponent =", first_number ** second_number)
print(" Floor Division =", first_number // second_number)