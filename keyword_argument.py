def print_full_name(**kwargs):
    print(kwargs)
    print(f"My full name is {kwargs['first_name']} {kwargs['last_name']}")

print_full_name(first_name="Avipsha", last_name="Shrestha", middle_name="None")