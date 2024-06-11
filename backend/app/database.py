



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
        return cursor.rowcount  # Returns the number of affected rows
    finally:
        connection.close()

# Check if the author exists
def author_exists(author_id):
    query = "SELECT AuthorID FROM Authors WHERE AuthorID = %s"
    result = execute_select_query(query, (author_id,))
    return bool(result)

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
    Books = execute_select_query(query)
    for book in Books:
        print(book)


    # AuthorID = 1
    # PublisherID = 1
    # # Insert a new book
    # #query = "INSERT INTO Books (Title, AuthorID, PublisherIDdesc) VALUES (%s, %s, %s)"
    # #params = ("New Book", "John Doe", "Publisher X")
    # query = "INSERT INTO Books (Title, AuthorID, PublisherID, Genre, PublicationYear, ISBN) VALUES (%s, %s, %s, %s, %s, %s)"
    # params = ("New Book", AuthorID, PublisherID, "Fiction", 2024, "1234567890")
    # rowcount = execute_write_query(query, params)
    # print(f"{rowcount} row(s) inserted")