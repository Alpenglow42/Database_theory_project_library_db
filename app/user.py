
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



# Execute an INSERT, UPDATE, or DELETE query
def execute_write_query(query, params=None):
    connection = connect_to_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        return cursor.rowcount  # Returns the number of affected rows
    finally:
        connection.close()

# new code
def register_user(username, password, email):
    query = "INSERT INTO Users (Username, Password, Email) VALUES (%s, %s, %s)"
    params = (username, password, email)
    rowcount = execute_write_query(query, params)
    return rowcount > 0

# Check if the author exists
def author_exists(author_id):
    query = "SELECT AuthorID FROM Authors WHERE AuthorID = %s"
    result = execute_select_query(query, (author_id,))
    return bool(result)

# Get user details
def get_user_details(username):
    query = "SELECT * FROM Users WHERE Username = %s"
    result = execute_select_query(query, (username,))
    return result

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

# Insert a new book
def insert_book(title, author_id, publisher_id, genre, publication_year, isbn):
    if author_exists(author_id):
        query = "INSERT INTO Books (Title, AuthorID, PublisherID, Genre, PublicationYear, ISBN) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (title, author_id, publisher_id, genre, publication_year, isbn)
        rowcount = execute_write_query(query, params)
        print(f"{rowcount} row(s) inserted")
    else:
        print("AuthorID does not exist.")


# Example usage
if __name__ == "__main__":
    # Fetch all books
    query = "SELECT * FROM Books"
    books = execute_select_query(query)
    for book in books:
        print(book)

    # Insert a new book
    AuthorID = 1
    PublisherID = 1
    insert_book("New Book", AuthorID, PublisherID, "Fiction", 2024, "1234567890")

    # Get user details
    user_details = get_user_details("johndoe")
    for detail in user_details:
        print(detail)




#old code
# from app.database import execute_select_query, execute_write_query
#
# # User registration
# def register_user(username, password, email):
#     query = "INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)"
#     params = (username, password, email)
#     rowcount = execute_write_query(query, params)
#     return rowcount > 0
#
# # User authentication
# def authenticate_user(username, password):
#     query = "SELECT * FROM Users WHERE username = %s AND password = %s"
#     params = (username, password)
#     result = execute_select_query(query, params)
#     return len(result) > 0
#
# # Get user details
# def get_user_details(username):
#     query = "SELECT * FROM users WHERE username = %s"
#     params = (username,)
#     result = execute_select_query(query, params)
#     if result:
#         return result[0]
#     else:
#         return None
#
# # Check if the user is an admin
# def is_admin(username):
#     user_details = get_user_details(username)
#     if user_details:
#         role = user_details[3]  # Assuming the role is stored in the 4th column
#         return role == 'admin'
#     return False
#
# # Example usage
# if __name__ == "__main__":
#     # Register a new user
#     success = register_user("johndoe", "password123", "john@example.com")
#     print(f"User registration successful: {success}")
#
#     # Authenticate a user
#     is_authenticated = authenticate_user("johndoe", "password123")
#     print(f"User authenticated: {is_authenticated}")
#
#     # Get user details
#     Users_details = get_Users_details("johndoe")
#     print(f"Users details: {Users_details}")
#
#     # Check if the user is an admin
#     is_admin_user = is_admin("johndoe")
#     print(f"Is admin: {is_admin_user}")