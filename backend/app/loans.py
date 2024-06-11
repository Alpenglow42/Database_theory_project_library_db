import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
        host="172.17.0.2",
        user="root",
        password="root",
        database="library_db"
    )
    return connection

def execute_select_query(query, params=None):
    connection = connect_to_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result
    finally:
        connection.close()

def execute_write_query(query, params=None):
    connection = connect_to_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        return cursor.rowcount
    finally:
        connection.close()

# Example functions to interact with the Loans table
def get_all_loans():
    query = "SELECT * FROM Loans"
    return execute_select_query(query)

def insert_loan(user_id, book_id, loan_date, return_date):
    query = "INSERT INTO Loans (UserID, BookID, LoanDate, ReturnDate) VALUES (%s, %s, %s, %s)"
    params = (user_id, book_id, loan_date, return_date)
    return execute_write_query(query, params)

# Example usage
if __name__ == "__main__":
    loans = get_all_loans()
    for loan in loans:
        print(loan)
