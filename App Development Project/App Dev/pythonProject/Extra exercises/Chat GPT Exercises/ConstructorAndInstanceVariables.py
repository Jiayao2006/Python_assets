class Book:
    def __init__(self, title = None, author = None):
        self.__title = title
        self.__author = author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def display_info(self):
        print(f"Title: {self.get_title()}, Author: {self.get_author()}")


book1 = Book()
book1.set_title("Harry Potter")
book1.set_author("JK Rowling")
book1.display_info()