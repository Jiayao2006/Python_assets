import shelve

class CustomError(Exception):
    def __init__(self, message:str):
        super().__init__(message)
        self.__message = message
    def __str__(self):
        return f"{self.__message}"


class ToDoList:
    status = ["Completed", "Pending"]
    def __init__(self, id, task, status):
        self.__id = id
        self.__task = task
        self.__status = status

    def get_id(self):
        return self.__id

    def get_task(self):
        return self.__task

    def get_status(self):
        return self.__status

    def set_id(self, id):
        self.__id = id

    def set_task(self, task):
        self.__task = task

    def set_status(self, status):
        self.__status = status

def add():
    try:
        id = input("Enter ID: ")
        task_description = input("Enter task: ")
        status = input("Enter status: ").capitalize()
        if status in ToDoList.status:
            task = ToDoList(id, task_description, status)
            with shelve.open("todolist") as db:
                db[id] = task
                print(f"Task {id} added successfully.")
        else:
            raise CustomError("Invalid Status, only 'Completed' and 'Pending' allowed.")

    except CustomError as e:
        print(e)
    except ValueError as e:
        print("Enter a valid ID")


def mark():
    try:
        id = input("Enter ID to mark as completed: ")
        with shelve.open("todolist") as db:
            if id in db:
                task = db[id]
                task.set_status("Completed")
                db[id] = task
                print(f"Task {id} marked as 'Completed'")
                print(f"Task {db[id].get_id()}. {db[id].get_task()}, Status: {db[id].get_status()}")
            else:
                raise CustomError("Task ID not found")
    except CustomError as e:
        print(e)
    except:
        print("Unknown Error Occurred")

def display():
    with shelve.open("todolist") as db:
        for key, value in db.items():
            print(f"Task {key}. {value.get_task()}, Status: {value.get_status()}")

def main():
    while True:
        try:
            print("-----To Do List-----")
            print("1. Add tasks")
            print("2. Mark Tasks")
            print("3. Display Tasks")
            print("4. Quit")
            command = int(input("Enter an option: "))
            if command == 1:
                add()
            elif command == 2:
                mark()
            elif command == 3:
                display()
            elif command == 4:
                break
            else:
                raise CustomError("Choose between 1-3")
        except CustomError as e:
            print(e)
        except ValueError as e:
            print("Wrong data format entered")


if __name__ == '__main__':
    main()



