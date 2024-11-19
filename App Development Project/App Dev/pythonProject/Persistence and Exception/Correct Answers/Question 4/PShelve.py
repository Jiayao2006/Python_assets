command = 0


def display_menu():
    while True:
        print("Select the program (1-6) to run: ")
        print("1. Search for a phone")
        print("2. Add a new phone")
        print("3. Update phone details")
        print("4. Delete a phone")
        print("5. Display all phones")
        print("6. Quit the program")
        val = int(input("Enter your command (1-6): "))
        if val == 6:
            print("End of program")
            break
        elif val == 1:
            search()
        elif val == 2:
            add()
        elif val == 3:
            update()
        elif val == 4:
            delete()
        elif val == 5:
            display_all()


def search():
    pass


def add():
    pass


def update():
    pass


def delete():
    pass


def display_all():
    pass


display_menu()
