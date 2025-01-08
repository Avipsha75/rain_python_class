#csv = comma separated values tsv = tab separated values
import csv

#File path for the sales tracker
file_path = "sales_tracker.csv"

#Create a new CSV file with headers
def create_csv():
    headers = ["Date", "Product", "Price per Unit", "Total"]
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Sales tracker created.")

#Add a new sale record to the CSV file
def add_sale(date, product, quantity, price_per_unit):
    total = quantity * price_per_unit
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, quantity, price_per_unit, total])
    print("Sale added successfully.")

#Calculate total sales from the CSV file
def calculate_total_sales():
    total_sales = 0 
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["Total"])
    print(f"Total Sales: ${total_sales:.2f}")

#Example usage
create_csv()
add_sale("2025-01-06", "Laptop", 2, 1200.50)
add_sale("2025-01-07", "Mouse", 5, 25.99)
calculate_total_sales()