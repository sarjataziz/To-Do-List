import datetime
import os

class Task:
    def __init__(self, description, is_complete = False, due_date = None, priority = None)
        self.description = description
        self.is_complete = is_complete
        self.due_date = due_date
        self.priority = priority

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.fileName = "My Task File.txt"
        self.load_tasks()
        
    def addTask(self, description):
        self.tasks.append(Task(description))
        print("Your Task Is Added Successfully")
    
    def completeTask(self, x):
        self.tasks[x].is_complete = True
        print("Your Task Mark Is Done")
    
    def viewTask(self):
        
        
        