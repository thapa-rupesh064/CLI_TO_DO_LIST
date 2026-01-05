# Terminal Based To do list project: 
tasks = [] # An empty list to store the tasks..
def add_task():
    task_name = input("Enter the task: ") # error handling 
    tasks.append({"task": task_name,"done": False})
    print("Task added successfully!")
def view_task():
    if ("to_do.txt" == ""):
        print("No task yet!")
    else:
        print("---- All Tasks ----")
        for i, task in enumerate(tasks, start=1):
            box = "✔" if task["done"] else " "  
            print(f"{i}. [{box}] {task['task']}")
    print("____________________")
def check_task():
    view_task()
    if tasks: 
        task_id = int(input("Enter task id to mark done: "))
        if 1 <= task_id <= len(tasks):
            tasks[task_id - 1]["done"] = True
            print(f"task no. {task_id} successfully marked done.")
            view_task()
        else:
            print("Invalid task number.")
def remove_task():
    view_task()
    task_id = int(input("Enter task id to remove: "))
    if 1 <= task_id <= len(tasks):
        removed_task = tasks.pop(task_id-1)
        print(f"Task no. {task_id} removed successfully!")
        view_task()
    else:
        print("Invalid task number!")

def main():
    while True:
        print("____TO DO LIST____")
        print("1.Add a task:")
        print("2.View all tasks.")
        print("3.Mark task done.")
        print("4.Remove a task.")
        print("5.Exit")
        print("___________________")
        choice = int(input("Enter a choice(1-5):"))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            check_task()
        elif choice == 4:
            remove_task()
        elif choice == 5:
            print("Exiting....")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()