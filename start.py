'''
1. add task
2. view task
3. mark done
4. remove task



'''
def add_task():
    pass

def view_task():
    pass

def check_task():
    pass

def remove_task():
    pass

def main():
    while True:
        print("____TO DO LIST____")
        print("1.Add a task:")
        print("2.View all tasks.")
        print("3.Mark task done.")
        print("4.Remove a task.")
        print("5.Exit")
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