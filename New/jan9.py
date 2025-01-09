#csv = comma separated values tsv = tab separated values
import csv
import random
import numpy as np


#Files name required in this task
sales_data_file = "sales_data.csv"
summary_data_file = "sales_summary.csv"

def create_csv():
    """
    Create a new CSV file with headers
    """
    headers = ["Product", "City", "Quantity", "Price", "Total"]
    with open(sales_data_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Sales summary created.")

#Add a new sale record to the CSV file
def add_sale(product, city, quantity, price):
    total = quantity * price
    with open(sales_data_file, mode ="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([product, city, quantity, price, total])
    print("Sale added successfully.")

#Calculate total sales from the CSV file
def calculate_total_sales():
    total_sales = 0 
    with open(sales_data_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["Total"])
    print(f"Total Sales: ${total_sales:.2f}")

def generate_random_sales_data(num_records):
    products = ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

    for _ in range(num_records):
        product = random.choice(products)
        city = random.choice(cities)
        quantity = random.randint(10, 500) #Random units sold
        price = random.uniform(10.0, 1000.0) #Random price
        add_sale(product, city, quantity, price)

    print(f"Generated {num_records} random sales records.")

def analyze_sales_data():
    sales_data = []
    #Read data from the sales CSV
    with open(sales_data_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Sales"] = int(row["Quantity"])
            row["Price"] = float(row["Price"])
            row["Revenue"] = row["Sales"] * row["Price"]
            sales_data.append(row)

    #Calculate metrics using NumPy
    revenues = np.array([row["Revenue"] for row in sales_data])
    average_revenue = np.mean(revenues)
    product_revenue_map = {row["Product"]: row["Revenue"] for row in sales_data}
    product_with_highest_revenue = max(product_revenue_map, key=product_revenue_map.get)
    region_revenue_map = {}
    for row in sales_data:
        region = row["City"]
        region_revenue_map[region] = region_revenue_map.get(region, 0) + row["Revenue"]

    #Write the summary to a new CSV
    with open(summary_data_file, mode = "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "City", "Sales", "Price", "Total"])
        for row in sales_data:
            writer.writerow([row["Product"], row["City"], row["Sales"], row["Price"], row["Total"]])

    #Print summary results
    print("\nAnalysis  Summary:")
    print(f"Average Revenue: ${average_revenue:.2f}")
    print(f"Product with Highest Revenue: {product_with_highest_revenue}(${product_revenue_map[product_with_highest_revenue]:.2f})")
    print("Total Revenue by Region:")
    for region, revenue in region_revenue_map.items():
        print(f" - {region}: ${revenue:.2f}")

create_csv() # sales_data.csv cretae with headers

generate_random_sales_data(100)

analyze_sales_data() 
    



