import threading

# Lock object for concurrency control
lock = threading.Lock()

# Acquire a lock
def acquire_lock():
    lock.acquire()
    return lock

# Release a lock
def release_lock(lock_obj):
    lock_obj.release()

# Execute a thread-safe database operation
def thread_safe_operation(operation, *args):
    lock.acquire()
    try:
        result = operation(*args)
        return result
    finally:
        lock.release()

# Example usage
if __name__ == "__main__":
    from app.database import execute_write_query

    # Function to simulate a database operation
    def insert_record(name):
        query = "INSERT INTO example_table (name) VALUES (%s)"
        params = (name,)
        rowcount = execute_write_query(query, params)
        print(f"Inserted {rowcount} row(s) with name {name}")

    # Create and start multiple threads
    threads = []
    for i in range(5):
        thread = threading.Thread(target=thread_safe_operation, args=(insert_record, f"Name {i}"))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()