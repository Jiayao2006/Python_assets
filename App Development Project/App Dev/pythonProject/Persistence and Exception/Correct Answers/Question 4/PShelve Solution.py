import shelve
from Phone import *

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
    phone_id = input("Enter the phone id to search: ")
    print(phone_dict[phone_id])


def add():
    phone_id = input("Enter phone id: ")
    make = input("Enter phone make: ")
    model = input("Enter phone model: ")
    price = input("Enter price of phone: ")

    phone = Phone()
    phone.set_id(phone_id)
    phone.set_make(make)
    phone.set_model(model)
    phone.set_price(price)
    phone_dict[phone.get_id()] = phone


def update():
    phone_id = input("Enter the phone id to update: ")

    phone = phone_dict.get(phone_id)
    input_make = input("What is the new make? (Leave empty to remain unchange): ")
    input_model = input("What is the new model? (Leave empty to remain unchange): ")
    input_price = input("What is the new price? (Leave empty to remain unchange): ")

    if len(input_make) > 0:
        phone.set_make(input_make)
        print(f"Phone: {phone_id} make updated")

    if len(input_model) > 0:
        phone.set_model(input_model)
        print(f"Phone: {phone_id} model updated")

    if len(input_price) > 0:
        phone.set_price(input_price)
        print(f"Phone: {phone_id} price updated")


def delete():
    phone_id = input("Enter the phone id to delete: ")
    phone_dict.pop(phone_id, None)
    print(f"Phone: {phone_id} is deleted")


def display_all():
    for key in phone_dict:
        print(phone_dict[key])


db = shelve.open("storage", "c")
phone_dict = {}
try:
    if "Phone" in db:
        phone_dict = db["Phone"]
    else:
        db["Phone"] = phone_dict
except:
    print("Error in opening storage.db")
else:
    display_menu()
