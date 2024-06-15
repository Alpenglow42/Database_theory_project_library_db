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

# Example functions to interact with the Publishers table
def get_all_publishers():
    query = "SELECT * FROM Publishers"
    return execute_select_query(query)

def insert_publisher(publisher_name):
    query = "INSERT INTO Publishers (PublisherName) VALUES (%s)"
    params = (publisher_name,)
    return execute_write_query(query, params)

# Example usage
if __name__ == "__main__":
    publishers = get_all_publishers()
    for publisher in publishers:
        print(publisher)
