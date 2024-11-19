import shelve

class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_year(self, year):
        self.__year = year

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

def add():
    title = input("Enter title of the book: ").capitalize()
    author = input("Enter author of the book: ").capitalize()
    year = int(input("Enter year of publication: "))
    book1 = Book(title, author, year)
    with shelve.open("book") as db:
        db[title] = book1
        print("Book added successfully")

def display():
    try:
        title = input("Enter title to display it's details: ").capitalize()
        with shelve.open("book") as db:
            if title in db:
                book = db.get(title)
                print(f"Title: {book.get_title()}, Author: {book.get_author()}, Year: {book.get_year()}")
            else:
                raise KeyError
    except KeyError:
        print("Title not found")

def delete():
    try:
        title  =  input("Enter title to delete: ").capitalize()
        with shelve.open("book") as db:
            if title in db:
                del db[title]
                print("Deleted successfully")
            else:
                raise KeyError
    except KeyError:
        print("Title not found")

def main():
    while True:
        try:
            print("-----Book Shelve-----")
            print("1. Add Books")
            print("2. Display Books")
            print("3. Delete Books")
            print("4. Quit")
            command = int(input("Enter an option (1-4):  "))
            if command == 1:
                add()
            elif command ==  2:
                display()
            elif command   == 3:
                delete()
            elif command == 4:
                break
            else:
                raise ValueError
        except ValueError:
            print("Incorrect data entered")
if __name__ == '__main__':
    main()