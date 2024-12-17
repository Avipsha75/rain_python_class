empty_list = [] #empty list

empty_list.append("apple") #add to list
empty_list.append("banana")
empty_list.append("apple")  #add to list
empty_list.append("banana")
print(empty_list) #print list

for index, fruit in enumerate(empty_list):               # or we can also write for fruit in (empty_list):
    print(f"Item position: {index} and value: {fruit}")  # print(empty_list)


