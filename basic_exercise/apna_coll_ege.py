# # Create a new file "practice.txt" using python. Add the following data in it.
# # Hi everyone
# # we are learing File I/O
# # using Java.
# # I like programming in Java.
# # WAF that replace all occurances of "Java" with "Python" in the file.
# # Search if the word "learning" exists in file or not.
# # with open("practice.txt", "w") as f:
# #     f.write("Hi everyone\n")
# #     f.write("we are learing File I/O\n")
# #     f.write("using Java.\n")
# #     f.write("I like programming in Java.\n")
# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\n")
#     f.write("we are learning File I/O\n")
#     f.write("using Java.\n")
#     f.write("I like programming in Java.\n")

# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)
#     new_data = data.replace("Java", "Python")
#     print(new_data)
    
# with open("practice.txt", "w") as f:
#         f.write(new_data)

# def check_for_word(data):
#     word = "learning"
#     if word in data:
#         print("Word found")
#     else:
#         print("Word not found")

# check_for_word(new_data)

# #WAF to find in which line of the file does  the word "learning" occur first.
# #Print -1 if the word is not found.
# def check_for_line(data):
#     word = "learning"
#     line_no = 1
#     with open("practice.txt","r") as f:
#          while data:
#             data = f.readline()
#             if word in data:
#                     print(line_no)
#                     line_no += 1
                
#     return -1
# check_for_line(data)

#From a file containing numbers separated by comma, print the count of even numbers.

count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    nums = data.split(",")  # Split the data into a list of strings
    for val in nums:
        if int(val) % 2 == 0:  # Convert each value to an integer
            count += 1
print(count)