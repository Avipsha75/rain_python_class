import csv

file_path = "sales_summary.csv"

# Step 1: Create the CSV file with headers
def create_csv():
    headers = ["Product", "Region", "Sales", "Price", "Total"]  # Added 'Total' column
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Sales summary created.")

# Step 2: Add a sale record to the CSV file
def add_sale(product, region, sales, price):
    total = sales * price  # Calculate total revenue for the product
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([product, region, sales, price, total])
    print(f"Sale added successfully: {product}, {region}, {sales}, {price}, {total}")

# Step 3: Calculate total sales from the CSV file
def calculate_total_sales():
    total_sales = 0
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["Total"])  # Sum up the 'Total' column
    print(f"Total Sales: ${total_sales:.2f}")

# Example Usage
create_csv()  # Create the CSV file
add_sale("Laptop", "Nepal", 100, 120000)  # Add sales record
add_sale("Computer", "India", 5, 25809.9)  # Add another sales record
calculate_total_sales()  # Calculate and display the total sales
