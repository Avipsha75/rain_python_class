import csv

file_path = "employee_data.csv"

def create_csv():
    headers =["Name", "Age", "Department"]
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Employee data saved successfully.")

def add_detail(name, age, department):
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, department])
    print("Employee detail added successfully.")

def generate_employee_data(num_records):
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]
    ages = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
    departments = ["HR", "Finance", "Engineering", "Marketing", "Sales"]

    for _ in range(num_records):
       for name, age, department in zip(names,ages, departments):
           add_detail(name, age, department)

    print("Employee data generated and saved successfully.")

def print_employees_above_30():
    with open(file_path, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            name, age, department = row
            if int(age) > 30:
                print(f"Name: {name}, Age: {age}, Department: {department}")

create_csv()
generate_employee_data(1)
print("\nEmployees above 30:")
print_employees_above_30()
