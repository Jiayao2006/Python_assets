import shelve


def main():
    while True:
        try:
            print("-----------Contact Book-----------")
            print("1. Add a contact")
            print("2. Display all contacts")
            print("3. Delete a contact")
            print("4. Quit")
            command = int(input("Enter an option (1-3): "))
            if command == 1:
                add()
            elif command == 2:
                display()
            elif command == 3:
                delete()
            elif command == 4:
                break
            else:
                raise ValueError

        except ValueError:
            print("Enter a valid option")

def add():
    try:
        name = input("Enter name: ")
        number = int(input("Enter phone number: "))
        with shelve.open("contacts") as db:
            db[name] = number
        print("Added successfully")

    except ValueError:
        print("Invalid data format entered")
    except:
        print("Unknown error occurred")


def display():
    try:
        with shelve.open("contacts") as db:
            for key, value in db.items():
                print(f"Name: {key}, Number: {value}")
    except IOError:
        print("Input/Output error occurred")
    except:
        print("Unknown error occurred")


def delete():
    try:
        name = input("Enter name to delete: ")
        with shelve.open("contacts") as db:
            if name in db:
                del db[name]
                print("Deleted successfully")
            else:
                raise KeyError

    except KeyError:
        print("Name not found in contacts")
    except IOError:
        print("Input/Output error occurred")
    except:
        print("Unknown error occurred")

if __name__ == '__main__':
    main()