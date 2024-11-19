class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def display_info(self):
        return f"Title: {self.__title}, Author: {self.__author}"


book1 = Book("Harry Potter", "JK Rowling")
print(book1.display_info())