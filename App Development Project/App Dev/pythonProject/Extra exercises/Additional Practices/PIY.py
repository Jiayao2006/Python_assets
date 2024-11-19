from week1 import *

phone_inventory = {}

def main():
    while True:
        try:
            print("Select the program (1-5) to run: ")
            print("1. Search for a phone")
            print("2. Add a new phone")
            print("3. Update phone details")
            print("4. Delete a phone")
            print("5. Quit the program")
            command = int(input("Enter your command (1-5): "))
            if command == 1:
                search()

            elif command == 2:
                add()

            elif command == 3:
                update()

            elif command == 4:
                delete()

            elif command == 5:
                break
        except:
            print("Please try again")


def search():
    id = input("Enter phone ID to search: ")
    try:
        if id in phone_inventory:
            phone = phone_inventory.get(id)
            print(phone.get_phone_info())
        else:
            raise KeyError

    except KeyError:
        print("ID not found. Try Again!")


def add():
    try:
        id = input("Enter your phone ID: ")
        make = input("Enter phone make: ")
        model = input("Enter phone model: ")
        price = input("Enter price of phone: ")

        phone = Phone()
        phone.set_id(id)
        phone.set_make(make)
        phone.set_model(model)
        phone.set_price(price)
        phone_inventory[id] = phone
        print("Phone successfully added.")

    except:
        print("Unknown Error. Try Again!")


def update():
    id = input("Enter phone id to update: ")
    make = input("What is the new make? (Leave empty to remain unchange): ")
    model = input("What is the new model? (Leave empty to remain unchange): ")
    price = input("What is the new price? (Leave empty to remain unchange): ")

    if len(make) > 0:
        phone = phone_inventory.get(id)
        phone.set_make(make)
        print(f"Phone: {id} make updated")

    if len(model) > 0:
        phone = phone_inventory.get(id)
        phone.set_model(model)
        print(f"Phone: {id} model updated")

    if len(price) > 0:
        phone = phone_inventory.get(id)
        phone.set_price(price)
        print(f"Phone: {id} price updated")


def delete():
    id = input("Enter the phone ID to delete: ")
    try:
        del phone_inventory[id]
        print(f"Phone {id} is deleted.")
    except KeyError:
        print("ID not found. Try Again!")

if __name__ == '__main__':
    main()
