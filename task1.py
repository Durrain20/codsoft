class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty.")

    def update_task(self, index, updated_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = updated_task
            print("Task updated successfully!")
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task removed successfully!")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '2':
            index = int(input("Enter task index to update: "))
            updated_task = input("Enter updated task: ")
            todo_list.update_task(index, updated_task)
        elif choice == '3':
            index = int(input("Enter task index to remove: "))
            todo_list.remove_task(index)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
