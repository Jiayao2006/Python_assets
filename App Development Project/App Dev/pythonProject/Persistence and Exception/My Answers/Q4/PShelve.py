from file import *
import shelve

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
    id = int(input("Enter the phone id to search: "))
    print(phone_dict[id])


def add():
    try:
        phone_id = int(input("Enter phone id: "))
        make = input("Enter phone make: ")
        model = input("Enter phone model: ")
        price = input("Enter price of the phone")

        phone = Phone()
        phone.set_make(make)
        phone.set_model(model)
        phone.set_price(price)
        phone.set_id(phone_id)
        phone_dict[phone.get_id()] = phone

    except ValueError:
        print("Incorrect data type entered")

def update():
    id = int(input("Enter the phone id to update: "))
    make = input("What is the new make? (Leave empty to remain unchange): ")
    model = input("What is the new model? (Leave empty to remain unchange): ")
    price = input("What is the new price? (Leave empty to remain unchange): ")

    phone = phone_dict.get(id)

    if len(make) > 0:
        phone.set_make(make)
        print(f"Phone: {id} make updated.")

    if len(model) > 0:
        phone.set_model(model)
        print(f"Phone: {id} model updated.")

    if len(price) > 0:
        phone.set_price(price)
        print(f"Phone: {id} price updated.")


def delete():
    phone_id = input("Enter the phone id to delete: ")
    phone_dict.pop(phone_id, None)
    print(f"Phone: {phone_id} is deleted")


def display_all():
    for key in phone_dict:
        print(phone_dict[key])


phone_dict = {}

display_menu()
