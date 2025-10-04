from tasks import tasks , max_tasks
from todo_functions import add_task , view_task , update_task, mark_done , delete_task

def menu():
    while True:
        print("\n -------- To-Do Application--------")
        print("1.Add Task")
        print("2.View Tasks")
        print("3.Update Task")
        print("4.Mark Task as Done")
        print("5.Delete Task")
        
        choice=input("enter your choice")
        
        if choice == "1":
            add_task(tasks, max_tasks)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()