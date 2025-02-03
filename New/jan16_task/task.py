from collections import deque

task = deque(f"{value}" for value in
             ["Assignment", "Make your bed", "Practice Maths", "Cook", "Practice Dance"])

task.append("Go to the gym")
task.append("Go to the market") 
task.append("Go to the library")
print(f"Task added: {task}")

task.popleft()
print(f"First task removed: {task}")
    
task.rotate(1)
print(f"Task rotated: {task}")


print("Task to be done:")
print(task)


