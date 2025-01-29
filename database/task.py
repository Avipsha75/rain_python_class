# Task: Design a simple to-do list with an SQL database.
# Create a table for tasks (ID, description, due date).
# Allow users to add, remove, and view tasks.
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)

engine = create_engine('sqlite:///todo_list.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_task(description):
    session.add(Task(description=description))
    session.commit()
    print(f"Task added: {description}")

def remove_task(task_id):
    task = session.get(Task, task_id)
    if task:
        session.delete(task)
        session.commit()
        print(f"Task {task_id} removed.")
    else:
        print("Task not found.")

def view_tasks():
    for task in session.query(Task).all():
        print(f"ID: {task.id}, Description: {task.description}")
while True:
    add_task(input("Enter a task: "))
    add_task("finish  the report")
    add_task("call mom")


    remove_task(6)
    
    user_choice = input("""
            Do you want to continue? Yes or No
            """)
    if user_choice.lower().strip() == "no": 
        view_tasks()
        break


