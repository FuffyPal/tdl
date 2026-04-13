import argparse
import sys
from src import todo
from src import storage

def menu():
    print("---Helloowww To Do List---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. List Tasks")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        return -1

def interactive_mode(data):
    while True:
        choice = menu()
        if choice == 1:
            key = todo.add()
            storage.save(key, data)
        elif choice == 2:
            key = todo.remove()
            storage.remove(key, data)
        elif choice == 3:
            key, new_value = todo.update()
            storage.update(key, new_value, data)
        elif choice == 4:
            todo.list(data)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    parser = argparse.ArgumentParser(description="To-Do List Application CLI")
    parser.add_argument('-a', '--add', type=str, metavar='TASK', help='Add a new task')
    parser.add_argument('-r', '--remove', type=str, metavar='TASK', help='Remove a task')
    parser.add_argument('-u', '--update', nargs=2, metavar=('TASK', 'STATUS'), help='Update task status (+=[true] or -=[false])')
    parser.add_argument('-l', '--list', action='store_true', help='List all tasks')

    if len(sys.argv) == 1:
        data = storage.load()
        interactive_mode(data)
        return

    args = parser.parse_args()
    data = storage.load()

    if args.add:
        storage.save(args.add, data)
    elif args.remove:
        storage.remove(args.remove, data)
    elif args.update:
        task, status = args.update
        if status == '+':
            val = 'true'
        elif status == '-':
            val = 'false'
        else:
            val = status
        storage.update(task, val, data)
    elif args.list:
        todo.list(data)

if __name__ == "__main__":
    main()