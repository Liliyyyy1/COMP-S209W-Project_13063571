from library_system import LibrarySystem


def print_menu():
    print("\n===== Library Management System =====")
    print("1. Add book")
    print("2. Add user")
    print("3. Show all books")
    print("4. Show all users")
    print("5. Borrow book")
    print("6. Return book")
    print("7. Show user's borrowed books")
    print("8. Search book by title")
    print("9. Remove book")
    print("10. Count total books")
    print("11. Count available books")
    print("12. Count borrowed books")
    print("13. Exit")


def load_sample_data(library):
    # Sample books
    library.add_book("B001", "Python Basics", "Tom")
    library.add_book("B002", "Java Programming", "Jerry")
    library.add_book("B003", "C++ Fundamentals", "Mike")
    library.add_book("B004", "Data Structures", "Alice")
    library.add_book("B005", "Database Systems", "John")

    # Sample users
    library.add_user("U001", "Anna", "student")
    library.add_user("U002", "Bob", "teacher")
    library.add_user("U003", "Chris", "general")


def main():
    library = LibrarySystem()
    load_sample_data(library)

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(book_id, title, author)

        elif choice == "2":
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            user_type = input("Enter user type (student/teacher/general): ").lower()
            library.add_user(user_id, name, user_type)

        elif choice == "3":
            library.show_books()

        elif choice == "4":
            library.show_users()

        elif choice == "5":
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            library.borrow_book(user_id, book_id)

        elif choice == "6":
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID: ")
            library.return_book(user_id, book_id)

        elif choice == "7":
            user_id = input("Enter user ID: ")
            library.show_user_borrowed_books(user_id)

        elif choice == "8":
            keyword = input("Enter book title keyword: ")
            library.search_book(keyword)

        elif choice == "9":
            book_id = input("Enter book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "10":
            library.count_books()

        elif choice == "11":
            library.count_available_books()

        elif choice == "12":
            library.count_borrowed_books()

        elif choice == "13":
            print("Exiting system. Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
