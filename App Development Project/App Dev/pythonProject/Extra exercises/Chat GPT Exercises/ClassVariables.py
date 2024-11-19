class Library:
    total_books = 0

    def __init__(self):
        Library.total_books += 1


asset = Library()
asset2 = Library()
asset3 = Library()
asset4 = Library()

print(Library.total_books)