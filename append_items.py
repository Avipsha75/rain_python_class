thislist = [1,2,3,4,5]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
    print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"] 
newlist = [x for x in fruits if "a" in x]
print(newlist)