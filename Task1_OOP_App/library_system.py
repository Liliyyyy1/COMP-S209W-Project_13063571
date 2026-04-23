from book import Book
from user import User, StudentUser, TeacherUser


class LibrarySystem:
    def __init__(self):
        self.__books = []
        self.__users = []

    def add_book(self, book_id, title, author):
        for book in self.__books:
            if book.get_book_id() == book_id:
                print("Book ID already exists.")
                return
        new_book = Book(book_id, title, author)
        self.__books.append(new_book)
        print("Book added successfully.")

    def add_user(self, user_id, name, user_type):
        for user in self.__users:
            if user.get_user_id() == user_id:
                print("User ID already exists.")
                return

        if user_type == "student":
            new_user = StudentUser(user_id, name)
        elif user_type == "teacher":
            new_user = TeacherUser(user_id, name)
        else:
            new_user = User(user_id, name)

        self.__users.append(new_user)
        print("User added successfully.")

    def show_books(self):
        if not self.__books:
            print("No books in the library.")
            return
        for book in self.__books:
            print(book)

    def show_users(self):
        if not self.__users:
            print("No users in the system.")
            return
        for user in self.__users:
            print(user)

    def find_book_by_id(self, book_id):
        for book in self.__books:
            if book.get_book_id() == book_id:
                return book
        return None

    def find_user_by_id(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                return user
        return None

    def borrow_book(self, user_id, book_id):
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(book_id)

        if user is None:
            print("User not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if book.is_borrowed():
            print("This book is already borrowed.")
            return

        if user.borrow_book(book):
            book.borrow_book()
            print("Book borrowed successfully.")
        else:
            print("User has reached the borrow limit.")

    def return_book(self, user_id, book_id):
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_id(book_id)

        if user is None:
            print("User not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if book.return_book():
            user.return_book(book)
            print("Book returned successfully.")
        else:
            print("This book was not borrowed.")

    def show_user_borrowed_books(self, user_id):
        user = self.find_user_by_id(user_id)

        if user is None:
            print("User not found.")
            return

        borrowed_books = user.get_borrowed_books()
        if not borrowed_books:
            print("This user has not borrowed any books.")
            return

        print(f"{user.get_name()} borrowed:")
        for book in borrowed_books:
            print(book)

    def search_book(self, keyword):
        found = False
        for book in self.__books:
            if keyword.lower() in book.get_title().lower():
                print(book)
                found = True

        if not found:
            print("No matching books found.")

    def remove_book(self, book_id):
        book = self.find_book_by_id(book_id)

        if book is None:
            print("Book not found.")
            return

        if book.is_borrowed():
            print("Cannot remove a borrowed book.")
            return

        self.__books.remove(book)
        print("Book removed successfully.")

  
    def count_books(self):
        print(f"Total books: {len(self.__books)}")


    def count_available_books(self):
        count = 0
        for book in self.__books:
            if not book.is_borrowed():
                count += 1
        print(f"Available books: {count}")


    def count_borrowed_books(self):
        count = 0
        for book in self.__books:
            if book.is_borrowed():
                count += 1
        print(f"Borrowed books: {count}")
