def print_result(*args, **kwargs):
    print(args)
    print(kwargs)
    result = 0
    for number in args:
        result += number
    print(f"My full name is {kwargs['first_name']} {kwargs['last_name']} and total marls = {result}")

print_result(10,20,30,40,50, first_name="Avipsha", last_name="Shrestha")