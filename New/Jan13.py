import csv
import os

file_path = "data.csv"

def create_csv():
    headers = ["Category", "Value1", "Value2", "Value3"] 
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("CSV file created.")
   
def add_data(category, value1, value2, value3):
    with open(file_path, mode ="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, value1, value2, value3])
    print("Data added successfully.")

def generate_random_data(num_records):
    data = [
        ["A", 10, 20, 30],
        ["B", 5, 15, 25],
        ["C", 8, 18, 28],
        ["D", 12, 22, 32]  
    ]
    for _ in range(num_records):
        for record in data:
             add_data(record[0], record[1], record[2], record[3])
    print(f"Generated and saved {len(data) * num_records} records to '{file_path}'.")

def parse_csv_for_totals(file_path):
    # Initialize containers for row and column totals
    row_totals = {}
    column_totals = {}

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row

        # Initialize column totals dictionary with column names
        for header in headers[1:]: # Skip the first column (Category)
            column_totals[header] = 0

        # Process rows
        for row in reader:
            category = row[0]  # First column is the category
            values = list(map(int, row[1:]))  # Convert the rest of the row to integers
            row_totals[category] = sum(values)

            # Update column totals
            for header, value in zip(headers[1:], values):
                column_totals[header] += value

    # Output results
    print("Row Totals:")
    for category, total in row_totals.items():
        print(f"{category}: {total}")
    
    print("\nColumn Totals:")
    for column, total in column_totals.items():  # Fixed Typo
        print(f"{column}: {total}")

# Execution
create_csv()
generate_random_data(3)
parse_csv_for_totals(file_path)



   

