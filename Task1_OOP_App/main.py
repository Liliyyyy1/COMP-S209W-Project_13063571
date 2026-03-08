class LibrarySystem:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)

def print_menu():
    print("1. Add book")
    print("2. Show books")
    print("3. Exit")

library = LibrarySystem()

while True:
    print_menu()
    choice = input("Choose: ")

    if choice == "1":
        book = input("Book name: ")
        library.add_book(book)
    elif choice == "2":
        library.show_books()
    elif choice == "3":
        break
