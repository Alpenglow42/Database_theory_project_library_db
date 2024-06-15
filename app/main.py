



import cmd
from app.user import register_user, authenticate_user, is_admin
from app.book import get_all_books, get_book_details, add_book, update_book, checkout_book, return_book
from app.concurrency import thread_safe_operation

class LibraryManager(cmd.Cmd):
    intro = "Welcome to the Library Management System. Type 'help' to see available commands."
    prompt = "(Library) "

    def do_register(self, args):
        """Register a new user: register <username> <password> <email>"""
        try:
            username, password, email = args.split()
            if register_user(username, password, email):
                print("User registered successfully.")
            else:
                print("Failed to register user.")
        except ValueError:
            print("Invalid arguments. Usage: register <username> <password> <email>")

    def do_login(self, args):
        """Login with username and password: login <username> <password>"""
        try:
            username, password = args.split()
            if authenticate_user(username, password):
                self.username = username
                self.is_admin = is_admin(username)
                print("Login successful.")
            else:
                print("Invalid username or password.")
        except ValueError:
            print("Invalid arguments. Usage: login <username> <password>")

    def do_list_books(self, args):
        """List all available books."""
        books = get_all_books()
        for book in books:
            print(book)

    def do_book_details(self, args):
        """Get details of a book: book_details <book_id>"""
        try:
            book_id = int(args)
            book_details = get_book_details(book_id)
            if book_details:
                print(book_details)
            else:
                print("Book not found.")
        except ValueError:
            print("Invalid book ID. Usage: book_details <book_id>")

    # def do_checkout(self, args):
    #     """Checkout a book: checkout <book_id>"""
    #     if not self.username:
    #         print("You must be logged in to checkout a book.")
    #         return
    #     try:
    #         book_id = int(args)
    #         checkout_success = thread_safe_operation(checkout_book, book_id, self.username)
    #         if checkout_success:
    #             print("Book checked out successfully.")
    #         else:
    #             print("Failed to checkout book. It may be unavailable.")
    #     except ValueError:
    #         print("Invalid book ID. Usage: checkout <book_id>")




    # Add more commands for other operations (e.g., return_book, add_book, update_book)

    def do_exit(self, args):
        """Exit the program."""
        print("Goodbye!")
        return True

if __name__ == "__main__":
    manager = LibraryManager()
    manager.cmdloop()