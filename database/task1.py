# Task: Make a book library manager that stores books in SQLite.
# Use SQLAlchemy to add, remove, and search for books.
# Query books by genre, author, or rating.
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///library.db")
Base = declarative_base()
session = sessionmaker(bind=engine)()

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    rating = Column(Float)

Base.metadata.create_all(engine)

def add_book(title, author, genre, rating=None):
    session.add(Book(title=title, author=author, genre=genre, rating=rating))
    session.commit()

def remove_book(book_id):
    book = session.get(Book, book_id)
    if book:
        session.delete(book)
        session.commit()

def search_books_by(field, value):
    return session.query(Book).filter(getattr(Book, field) == value).all()

if __name__ == "__main__":
    add_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 4.5)
    add_book("1984", "George Orwell", "Dystopian", 4.8)
    add_book("To Kill a Mockingbird", "Harper Lee", "Classic", 4.9)
    
    for book in search_books_by("author", "George Orwell"):
        print(book.title)