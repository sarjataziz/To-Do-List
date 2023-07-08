import datetime

class Task:
    def __init__(self, description, priority=None, due_date=None, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added successfully!")

    def complete_task(self, task_number):
        if task_number >= 1 and task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.completed = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if task_number >= 1 and task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task removed successfully!")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        
        print("To-Do List:")
        for i, task in enumerate(self.tasks):
            status = "[X]" if task.completed else "[ ]"
            print(f"{i+1}. {status} {task.description}")

def main():
    manager = ToDoListManager()
    while True:
        print("1. Add a task")
        print("2. Complete a task")
        print("3. View to-do list")
        print("4. Remove a task")
        print("5. Save the task list to file")
        print("6. Add priority to task")
        print("7. Add due date to task")
        print("8. Sort tasks by due date")
        print("9. Exit")
        choice = int(input("Enter your choice (1-9): "))
        
        if choice == 1:
            description = input("Enter task description: ")
            manager.add_task(description)
        elif choice == 2:
            task_number = int(input("Enter the task number to mark as complete: "))
            manager.complete_task(task_number)
        elif choice == 3:
            manager.view_tasks()
        elif choice == 4:
            task_number = int(input("Enter the task number to remove: "))
            manager.remove_task(task_number)
        elif choice == 5:
            
        elif choice == 6:
            
        elif choice == 7:

        elif choice == 8:

        elif choice == 9:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

