import shelve

def add():
    try:
        id = input("Enter ID: ")
        name = input("Enter student name: ")
        score = int(input("Enter your score: "))
        with shelve.open("student") as db:
            db[id] = [name, score]
            print("Added Successfully\n")
    except ValueError:
        print("Data type is incorrect")


def update():
    try:
        id = input("Enter ID to update:  ")
        with shelve.open("student") as db:
            if id in db:
                record  = db[id]
                grade = int(input("Enter new grades: "))
                record[1] = grade
                db[id] = record
                print(f"ID: {id}, Name: {db[id][0]}, Score: {db[id][1]}")
                print("Grades changed successfully\n")
            else:
                raise KeyError
    except KeyError:
        print("ID not found")
    except ValueError:
        print("Data type is incorrect")


def display():
    with shelve.open("student") as db:
        for key, value in db.items():
            print(f"ID: {key}, Name: {value[0]}, Score: {value[1]}")

def main():
    while True:
        try:
            print("-----Student Records-----")
            print("1. Add Student Records")
            print("2. Update Student Records")
            print("3. Display Student Record")
            print("4. Quit")
            command = int(input("Enter your choice (1-4): "))
            if command == 1:
                add()
            elif command == 2:
                update()
            elif command == 3:
                display()
            elif command == 4:
                break
            else:
                raise ValueError
        except ValueError:
            print("Data type is incorrect")

if __name__ == '__main__':
    main()


