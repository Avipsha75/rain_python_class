"""
#Print numbers from 1 to 100.
count = 1
while count <= 100:
    print(count)
    count += 1

#Print numbers from 100 to 1.
count = 100
while count >= 1: #stopping condition
    print(count)
    count -= 1

#Print the multiplication table of a number n.
count = 1
n = int(input("Enter a number: "))
while count <= 10:
    mul = n * count
    print(f"{n} * {count} = {mul}")
    count += 1

#Print the square of numbers upto 10.
count = 1
while count <= 10:
    square = count**2
    print(square)
    count += 1

#Print the elements of the following list usinga loop: 
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number you want to find: "))
i = 0
while i < len(nums):
    if(nums[i]==x):
        print("Found at idx", i)
        break
    else:
        print("Finding...")
    i += 1

#using for
#Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in list:
    print(i)

#Search for a number x in this tuple using loop:
(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number you want to find: "))
idx = 0
for i in nums:
    if(i==x):
        print("Found at idx", idx)
        break #It is compulsory
    idx += 1

#using for and range()
#Print numbers from 1 to 100.
for i in range(1, 101):
    print(i)

#Print numbers from 100 to 1.
for i in range(100, 0, -1):
    print(i)

#Print the multiplication table of a number n.
n = int(input("Enter a number: "))
for i in range(1, 11):
    mul = n * i
    print(f"{n} * {i} = {mul}")

#WAP to find the sum of first n natural numbers.(using while loop)
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
    print("Total sum is", sum)

#WAP to find the factorial of first n natural numbers.(using for loop)
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
    print("Factorial is", fact)


#WAF to print the length of a list. (list is the parameter)
cities = ["Kathmandu", "Pokhara", "Bhaktapur", "Lalitpur", "Kritipur"]
heroes = ["Batman", "Superman", "Wonder Woman", "Aquaman", "Flash"]
def length(list):
    print(len(list))
print(length(cities))
print(length(heroes))

#wAF to print the elements of a list in a single line. (list is the parameter)
cities = ["Kathmandu", "Pokhara", "Bhaktapur", "Lalitpur", "Kritipur"]
heroes = ["Batman", "Superman", "Wonder Woman", "Aquaman", "Flash"]
def print_list(list):
    for item in list:
        print(item, end=" ")
print(print_list(cities))
print(print_list(heroes))

#WAF to find the factorial of n. (n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    print(fact)
cal_fact(5)

#WAF to take an input and check if it is odd or even.
def odd_even(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
odd_even(12)

#WARF to calculate the sum of first n natural numbers.
def calc_sum(n):
    if (n == 0):
        return 0
    calc_sum(n-1)
    return n + calc_sum(n-1)
sum = calc_sum(10)
print(sum)

#WARF to print all elements of a list.
#Hint: use list and index as parameters.
def print_list(list, index):
    if index == len(list):
        return
    print(list[index])
    print_list(list, index+1)
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print_list(fruits, 0)

values = {
    ("float", 9.0),
    ("int", 9)}
print(values)

"""

# Create a new file "practice.txt" using python. Add the following data in it.
# Hi everyone
# we are learing File I/O
# using Java.
# I like programming in Java.
# WAF that replace all occurances of "Java" with "Python" in the file.
# Search if the word "learning" exists in file or not.
# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\n")
#     f.write("we are learing File I/O\n")
#     f.write("using Java.\n")
#     f.write("I like programming in Java.\n")
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)
    new_data = data.replace("Java", "Python")
    print(new_data)
    
with open("practice.txt", "w") as f:
        f.write(new_data)
        def check_for_word():
              word = "learning"
              if word in data:
                  print("Word found")
              else:
                  print("Word not found")
