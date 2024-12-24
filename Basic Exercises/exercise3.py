# To calculate area and perimeter of shapes
while True:
    user_choice = input("""
        Please choose your option
        1. Circle
        2. Rectangle
        3. Triangle
        """)
    if user_choice == "1":
        r = float(input("Enter the radius:"))
        pi = 22 / 7
        area = pi * (r ** 2)
        circumference = 2 * pi * r
        print(f"The area of the circle is {area} and the circumference is {circumference} ")
    elif user_choice == "2":
        l = float(input("Enter the length:"))
        b = float(input("Enter the breadth"))
        a = l * b
        p = 2 * (l + b)
        print(f"The area of the rectangle is {a} and the perimeter is {p}")
    elif user_choice == "3":
        b = float(input("Enter the bae of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        a = 0.5 * b * h
        p = b + h
        print(f" The area of triangle is {a}, Perimeter: {p}")
    else:
        print("Invalid input")
    user_choice = input("""
    Do you want to continue? yes or no
    """)
    if user_choice.lower().strip() == "no":
        print("Thank you for using the calculator. Goodbye!")
        break
        




