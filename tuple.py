fruits = ("apple", "banana", "cherry,", "orange", "kiwi", "melon", "mango")
print(fruits[1]) #print second item
(green, *yellow, red) =  fruits
print(green, yellow, red)

fruits = {"apple", "banana", "cherry", "strawberry", "raspberry"}

for item in fruits:
    print(item)

fruits.add("apple")
print(fruits)