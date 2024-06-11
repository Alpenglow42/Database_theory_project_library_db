import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from book import add_book, checkout_book
from user import register_user, get_user_details


def add_user():
    print("Add a new user")
    username = input("Enter user name: ")
    password = input("Enter user password: ")
    email = input("Enter user email: ")
    if register_user(username, password, email):
        print("User added successfully!")
    else:
        print("Failed to add user.")


# def add_new_book():
#     print("Add a new book")
#     title = input("Enter book title: ")
#     author = input("Enter author name: ")
#     publisher = input("Enter publisher name: ")
#     if add_book(title, author, publisher):
#         print("Book added successfully!")
#     else:
#         print("Failed to add book.")

def add_new_book():
    print("Add a new book")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    publisher = input("Enter publisher name: ")
    genre = input("Enter book genre: ")
    publication_year = int(input("Enter publication year: "))
    isbn = input("Enter ISBN: ")
    if add_book(title, author, publisher, genre, publication_year, isbn):
        print("Book added successfully!")
    else:
        print("Failed to add book.")

def checkout_a_book():
    print("Checkout a book")
    book_id = input("Enter book ID: ")
    user_id = input("Enter user ID: ")
    if checkout_book(book_id):
        print("Book checked out successfully!")
    else:
        print("Failed to checkout book. It might be unavailable.")




def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add User")
        print("2. Add Book")
        print("3. Checkout Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            add_new_book()
        elif choice == '3':
            checkout_a_book()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()
