#WAP that allows a librarian to add several books to a library.For each book,ask the user to enter its title and the number of copies.Store each book and its available copy count in a dictionary.
"""
After the books have been added, display a menu that lets the user isssue a book, return a book, display all books or exit the program.
Apply these conditions:
Book titles should be compared without distinguishing uppercase and lowercase letters.
A book can be isssued only if it exists in the library and at least one copy is available.
Isssuing a book decreases its available copy count by one.
A book can be returned only if it exists in the library and atleast one copy has already been isssued.
Returning a book increases its available copy count by one.
Display an appropriate message for an unavailable book, an invalid choice or an invalid number of copies. 
"""


class Library:
    def __init__(self):
        self.books = {}

    def add_books(self):
        n = int(input("Enter the number of books to add: "))

        for i in range(n):
            title = input("Enter book title: ").strip().lower()
            copies = int(input("Enter number of copies: "))

            if copies <= 0:
                print("Invalid number of copies!")
                continue

            if title in self.books:
                self.books[title]["total"] += copies
                self.books[title]["available"] += copies
            else:
                self.books[title] = {
                    "total": copies,
                    "available": copies
                }

    def issue_book(self):
        title = input("Enter book title to issue: ").strip().lower()

        if title not in self.books:
            print("Book does not exist in the library.")
        elif self.books[title]["available"] > 0:
            self.books[title]["available"] -= 1
            print("Book issued successfully.")
        else:
            print("No copies available for issuing.")

    def return_book(self):
        title = input("Enter book title to return: ").strip().lower()

        if title not in self.books:
            print("Book does not exist in the library.")
        elif self.books[title]["available"] < self.books[title]["total"]:
            self.books[title]["available"] += 1
            print("Book returned successfully.")
        else:
            print("No book has been issued to return.")

    def display_books(self):
        if not self.books:
            print("Library is empty.")
            return

        print("\n--- Books in the Library ---")
        for title, details in self.books.items():
            print("Title:", title.title())
            print("Total copies:", details["total"])
            print("Available copies:", details["available"])
            print()

    def menu(self):
        while True:
            print("\n--- Library Menu ---")
            print("1. Issue a book")
            
class Library:
    def __init__(self):
        self.books = {}

    def add_books(self):
        n = int(input("Enter the number of books to add: "))

        for i in range(n):
            title = input("Enter book title: ").strip().lower()
            copies = int(input("Enter number of copies: "))

            if copies <= 0:
                print("Invalid number of copies!")
                continue

            if title in self.books:
                self.books[title]["total"] += copies
                self.books[title]["available"] += copies
            else:
                self.books[title] = {
                    "total": copies,
                    "available": copies
                }

    def issue_book(self):
        title = input("Enter book title to issue: ").strip().lower()

        if title not in self.books:
            print("Book does not exist in the library.")
        elif self.books[title]["available"] > 0:
            self.books[title]["available"] -= 1
            print("Book issued successfully.")
        else:
            print("No copies available for issuing.")

    def return_book(self):
        title = input("Enter book title to return: ").strip().lower()

        if title not in self.books:
            print("Book does not exist in the library.")
        elif self.books[title]["available"] < self.books[title]["total"]:
            self.books[title]["available"] += 1
            print("Book returned successfully.")
        else:
            print("No book has been issued to return.")

    def display_books(self):
        if not self.books:
            print("Library is empty.")
            return

        print("\n--- Books in the Library ---")
        for title, details in self.books.items():
            print("Title:", title.title())
            print("Total copies:", details["total"])
            print("Available copies:", details["available"])
            print()

    def menu(self):
        while True:
            print("\n--- Library Menu ---")
            print("1. Issue a book")
            print("2. Return a book")
            print("3. Display all books")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.issue_book()
            elif choice == "2":
                self.return_book()
            elif choice == "3":
                self.display_books()
            elif choice == "4":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice!")


library = Library()
library.add_books()
library.menu()
