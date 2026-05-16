tasks = []
while True:
    print("\n"*2)
    print("1.add task")
    print("2.show tasks")
    print("3.delete task")
    print("4.quit")
    choice = input("choose: ")
    if choice == "1":
        task = input("enter the task to add: ")
        tasks.append(task)
        print(tasks)
    elif choice == "2":
        for task in tasks :
            print(task)
    elif choice == "3":
        task = input("enter the task to delete : ")
        tasks.remove(task)
        print(tasks)
    else:
        print("quit the task")
        break
