import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

connection = sqlite3.connect("store.db")
cursor = connection.cursor()

# Create a table for products
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title STRING REQUIRED,
    author STRING REQUIRED,
    price FLOAT REQUIRED
)''')

# Insert data
cursor.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", ("HP", "JK", 99.99))
cursor.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", ("Stone", "Rowlling", 9.99))
cursor.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", ("Chamber", "Shrez", 10.99))
connection.commit()

# Fetch data
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)

connection.close()

    