import datetime
import os

class Task:
    def __init__(self, description, is_complete = False, due_date = None, priority = None):
        self.description = description
        self.is_complete = is_complete
        self.due_date = due_date
        self.priority = priority

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.fileName = "My Task File.txt"
        self.loadTasks()
        
    def addTask(self, description):
        self.tasks.append(Task(description))
        print("----------------Your Task Is Added Successfully-----------------")
    
    def completeTask(self, x):
        self.tasks[x].is_complete = True
        print("------------------Your Task Mark Is Done-------------------")
    
    def viewTask(self):
        self.tasks.sort(key = lambda x: (x.due_date is None, x.due_date))
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. [{'X' if task.is_complete else ' '}] {task.description}")
            
    def removeTask(self, index):
        self.tasks.pop(index)
        print("---------------Your Task Has Been Removed Successfully!-------------------")
    
    def addPriority(self, index, priority):
        self.tasks[index].priority = priority
        print("-------------------Priority added to the task!------------------------")
        
    def addDueDate(self, index, deu_date):
        self.tasks[index].deu_date = deu_date
        print("---------------Due date added into the task--------------------")
        
    def saveFile(self):
        try:
            with open(self.fileName, 'w') as file:
                for task in self.tasks:
                    file.write(f"{task.description}, {task.is_complete}, {task.deu_date}, {task.priority}\n")
            print(f"Your Task List Saved To {self.file}")
        
        except Exception as e:
            print("\n", e, "\n ----------------YOUR TASK FILE CAN'T SAVE---------------------")
            print("----------------------Please, try again----------------------")
            
    def loadTasks(self):
        try:
            if os.path.exists(self.fileName):
                with open(self.fileName, 'r') as file:
                    for line in file:
                        description, is_complete, due_date, priority = line.strip().split(',')
                        self.tasks.append(Task(description, is_complete == 'True', due_date if due_date != 'None' else None, int(priority) if priority != 'None' else None))
        except Exception as e:
            print("\n", e, "\n ----------------YOUR TASK FILE CAN'T LOAD---------------------")
            print("----------------Please, try again---------------------")
                    
            
def main():
    toDoList = ToDoList()
    try:
        while True:
            print("\nTo-Do List Manager\n"
                      "------------------\n"
                      "1. Add a task\n"
                      "2. Complete a task\n"
                      "3. View to-do list sorted by due date\n"
                      "4. Remove a task\n"
                      "5. Save the task list to file\n"
                      "6. Add priority to task\n"
                      "7. Add due date to task\n"
                      "8. Exit\n")
            
            choice = int(input("Enter your choice (1-8): "))
            
            match choice:
                case 1:
                    tasks_description = input("Enter the task description: ")
                    toDoList.addTask(tasks_description)
                    break;
                case 2:
                    task_number = int(input("Enter the task number for mark as complete: ")) - 1
                    toDoList.competeTask(task_number)
                    break
                case 3:
                    toDoList.viewTask()
                    break
                case 4:
                    task_numer = int(input("Enter the task number to remove: ")) - 1
                    toDoList.removeTask(task_number)
                    break
                case 5:
                    toDoList.saveFile()
                    break
                case 6:
                    break
                case 7:
                    break
                case 8:
                    toDoList.saveFile()
                    break

         
    except Exception as e:
        print("\n", e, "\nPlease Fix It First")
            
if __name__ == "__main__":
    main()                                          
                    
                        