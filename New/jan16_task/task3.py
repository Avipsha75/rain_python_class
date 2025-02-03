from collections import defaultdict

inventory = defaultdict(list)

inventory["Fruits"].append("Apple")
inventory["Fruits"].append("Banana")
inventory["Vegetables"].append("Carrot")
inventory["Vegetables"].append("Broccoli")

print(inventory)