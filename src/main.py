from todo.repository import TaskRepository
from todo.service import TaskService
from todo.cli import TodoCLI

def main():
    repo = TaskRepository()
    service = TaskService(repo)
    cli = TodoCLI(service)

    while True:
        command = input("todo> ").strip()

        if command == "add":
            cli.add()
        elif command == "list":
            cli.list_tasks()
        elif command == "exit":
            break
        else:
            print("Commands: add, list, exit")

if __name__ == "__main__":
    main()

        elif command.startswith("delete"):
            parts = command.split()
            if len(parts) != 2:
                print("Usage: delete <id>")
            else:
                cli.delete(int(parts[1]))

        elif command.startswith("complete"):
            parts = command.split()
            if len(parts) != 2:
                print("Usage: complete <id>")
            else:
                cli.complete(int(parts[1]))

        elif command.startswith("update"):
            parts = command.split()
            if len(parts) != 2:
                print("Usage: update <id>")
            else:
                cli.update(int(parts[1]))

