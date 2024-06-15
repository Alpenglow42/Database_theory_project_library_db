from app.database import execute_select_query, execute_write_query
from app.concurrency import acquire_lock, release_lock
from datetime import date, timedelta

import mysql.connector


# Connect to the MySQL database
def connect_to_db():
    connection = mysql.connector.connect(
        host="172.17.0.2",
        user="root",
        password="root",
        database="library_db"
    )
    return connection


# Execute a SELECT query
def execute_select_query(query, params=None):
    connection = connect_to_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result
    finally:
        connection.close()


# Execute an INSERT, UPDATE, or DELETE query
def execute_write_query(query, params=None):
    connection = connect_to_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        return cursor.rowcount, cursor.lastrowid  # Returns the number of affected rows and last inserted id
    finally:
        connection.close()


# Get author ID by name
def get_author_id(author_name):
    query = "SELECT AuthorID FROM Authors WHERE AuthorName = %s"
    result = execute_select_query(query, (author_name,))
    if result:
        return result[0][0]
    return None


# Get publisher ID by name
def get_publisher_id(publisher_name):
    query = "SELECT PublisherID FROM Publishers WHERE PublisherName = %s"
    result = execute_select_query(query, (publisher_name,))
    if result:
        return result[0][0]
    return None


# Add a new author
def add_author(author_name):
    query = "INSERT INTO Authors (AuthorName) VALUES (%s)"
    rowcount, author_id = execute_write_query(query, (author_name,))
    return author_id


# Add a new publisher
def add_publisher(publisher_name):
    query = "INSERT INTO Publishers (PublisherName) VALUES (%s)"
    rowcount, publisher_id = execute_write_query(query, (publisher_name,))
    return publisher_id


# Insert a new book
def add_book(title, author_name, publisher_name, genre, publication_year, isbn):
    author_id = get_author_id(author_name)
    if not author_id:
        author_id = add_author(author_name)

    publisher_id = get_publisher_id(publisher_name)
    if not publisher_id:
        publisher_id = add_publisher(publisher_name)

    # Get the 'AVB' status ID
    avb_status_id = execute_select_query("SELECT BookStatusID FROM BookStatus WHERE StatusDescription = 'avb'")[0][0]

    query = "INSERT INTO Books (Title, AuthorID, PublisherID, Genre, PublicationYear, ISBN) VALUES (%s, %s, %s, %s, %s, %s)"
    params = (title, author_id, publisher_id, genre, publication_year, isbn,)
    rowcount, _ = execute_write_query(query, params)

    return rowcount > 0

# Checkout a book
def checkout_book(book_id):
    connection = connect_to_db()
    try:
        cursor = connection.cursor()
        cursor.execute("START TRANSACTION")

        # Check if the book exists in the Books table
        cursor.execute("SELECT * FROM Books WHERE BookID = %s", (book_id,))
        book = cursor.fetchone()

        if book:
            # Update the BookStatus table if the book exists
            cursor.execute("UPDATE BookStatus SET bookstatus = 'Navb' WHERE BookID = %s", (book_id,))
            connection.commit()
            print("Book with ID", book_id, "has been checked out successfully.")
        else:
            print("Book with ID", book_id, "does not exist.")

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        # Close connection
        if connection.is_connected():
            cursor.close()
            connection.close()





# def checkout_book(book_id, user_id):
#     # Assuming the status description for "checked out" is 'checked out' and "available" is 'available'
#     update_status_query = """
#     UPDATE Books
#     SET BookStatusID = (SELECT BookStatusID FROM BookStatus WHERE StatusDescription = 'checked out')
#     WHERE BookID = %s AND BookStatusID = (SELECT BookStatusID FROM BookStatus WHERE StatusDescription = 'available')
#     """
#     status_params = (book_id,)
#     rowcount, _ = execute_write_query(update_status_query, status_params)
#
#     return rowcount > 0



# def checkout_book(book_id, user_id):
#     # Assuming the status ID for "checked out" is 2
#     query = "UPDATE Books SET BookStatusID = %s, CheckedOutBy = %s WHERE BookID = %s AND BookStatusID = 1"
#     params = (2, user_id, book_id)
#     rowcount, _ = execute_write_query(query, params)
#     return rowcount > 0

# Checkout a book
# def checkout_book(book_id, user_id):
#     query = "UPDATE Books SET CheckedOutBy = %s WHERE BookID = %s AND CheckedOutBy IS NULL"
#     params = (user_id, book_id)
#     rowcount, _ = execute_write_query(query, params)
#     return rowcount > 0

# old code
# # Get all books
# def get_all_books():
#     query = "SELECT * FROM Books"
#     result = execute_select_query(query)
#     return result
#
# # Get book details
# def get_book_details(book_id):
#     query = "SELECT * FROM Books WHERE id = %s"
#     params = (book_id,)
#     result = execute_select_query(query, params)
#     if result:
#         return result[0]
#     else:
#         return None
#
# # Add a new book
# def add_book(title, author, publisher):
#     query = "INSERT INTO Books (title, author, publisher) VALUES (%s, %s, %s)"
#     params = (title, author, publisher)
#     rowcount = execute_write_query(query, params)
#     return rowcount > 0
#
# # Update book details
# def update_book(book_id, title=None, author=None, publisher=None):
#     query = "UPDATE books SET "
#     params = []
#     if title:
#         query += "title = %s, "
#         params.append(title)
#     if author:
#         query += "author = %s, "
#         params.append(author)
#     if publisher:
#         query += "publisher = %s, "
#         params.append(publisher)
#     query = query.rstrip(", ") + " WHERE id = %s"
#     params.append(book_id)
#     rowcount = execute_write_query(query, params)
#     return rowcount > 0
#
# # Checkout a book
# def checkout_book(book_id, user_id):
#     lock = acquire_lock()  # Acquire a lock for concurrency control
#     try:
#         # Check if the book is available
#         query = "SELECT status FROM book_status WHERE book_id = %s"
#         params = (book_id,)
#         result = execute_select_query(query, params)
#         if result and result[0][0] == 'available':
#             # Update the book status to 'checked_out'
#             query = "UPDATE book_status SET status = 'checked_out' WHERE book_id = %s"
#             params = (book_id,)
#             execute_write_query(query, params)
#             # Insert a new loan record
#             query = "INSERT INTO loans (book_id, user_id) VALUES (%s, %s)"
#             params = (book_id, user_id)
#             execute_write_query(query, params)
#             return True
#         else:
#             return False
#     finally:
#         release_lock(lock)  # Release the lock
#
# # Return a book
# def return_book(book_id):
#     lock = acquire_lock()  # Acquire a lock for concurrency control
#     try:
#         # Update the book status to 'available'
#         query = "UPDATE book_status SET status = 'available' WHERE book_id = %s"
#         params = (book_id,)
#         execute_write_query(query, params)
#         # Remove the loan record
#         query = "DELETE FROM loans WHERE book_id = %s"
#         params = (book_id,)
#         execute_write_query(query, params)
#         return True
#     finally:
#         release_lock(lock)  # Release the lock