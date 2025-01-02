#Handling division by zero
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Exception:", e) #Output: Exception: division by zero

try:
    my_list = [1,2,3]
    print(my_list[5])
except IndexError as e:
    print("Exception:", e) #Output: Exception: list index out of range 