class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._borrowed_books = []

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_borrowed_books(self):
        return self._borrowed_books

    def get_borrow_limit(self):
        return 2

    def borrow_book(self, book):
        if len(self._borrowed_books) < self.get_borrow_limit():
            self._borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)

    def __str__(self):
        return f"User ID: {self._user_id}, Name: {self._name}, Type: General User"


class StudentUser(User):
    def get_borrow_limit(self):
        return 2

    def __str__(self):
        return f"User ID: {self._user_id}, Name: {self._name}, Type: Student"


class TeacherUser(User):
    def get_borrow_limit(self):
        return 5

    def __str__(self):
        return f"User ID: {self._user_id}, Name: {self._name}, Type: Teacher"
