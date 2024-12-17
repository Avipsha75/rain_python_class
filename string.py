x = "What's your name?"
print(x)

for x in "banana":
  print(x)

a = "Hello, World!"
print("Length ===", len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("discount" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[:-5])

b = "Hello, World!"
print(b[-2:])

print(b.upper()) #It is used in titles of newspaper and all.
print(b.lower()) #It is used in the gamings and all in username.
print(b.capitalize())

b = "  Hello, World!" # It is used to remove whitespace
print(b.strip())

b = "Hello, World!"
print(b.replace("World", "Universe"))

z = b.split(",") # It is used while making form to separate the first and last name.
print(z)

#There are three ways to print. They are:
name = input("Enter your name: ")
print("You have entered your name = " + name) #string concant
print(f"You have entered your name = {name}") #format string
print("You have entered your name = %s" % (name)) #Modulus string