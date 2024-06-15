# Database_theory_project_library_db
Library Management System
Overview

The Library Management System is a Python-based application designed to manage a library's operations through a MySQL database backend. It allows librarians to add new books, register users, and facilitate book checkouts. This README provides an overview of the project's design, functionality, and basic usage instructions.
Features

    Add Book: Enables librarians to add new books to the library database.
    Register User: Allows librarians to register new users into the system.
    Checkout Book: Facilitates the process of checking out books to registered users.

Project Structure

The project is structured into several key components:

    Backend: Handles database interactions and business logic.
    Frontend: Provides a command-line interface (CLI) for users to interact with the system.
    Database Schema: Defines the structure of tables and relationships in the MySQL database.

Design

The application follows a client-server architecture where the Python backend interacts with a MySQL database. Key design decisions include:

    Use of Python's mysql.connector for database connectivity.
    Separation of concerns between database operations (database.py), frontend CLI (main.py), and concurrency management (concurrency.py).

Usage
Prerequisites

    Python 3.x
    MySQL server

Installation

    Clone the repository:

    bash

git clone https://github.com/Alpenglow42/Database_theory_project_library_db.git
cd Database_theory_project_library_db

Install dependencies:

bash

    pip install mysql-connector-python

Setup

    Ensure MySQL server is running.
    Import the database schema (library_db.sql) into your MySQL server to create the necessary tables and relationships.

Running the Application

    Navigate to the project directory:

    bash

cd Database_theory_project_library_db

Start the application:

bash

    python main.py

    Follow the prompts in the command-line interface to perform actions like adding books, registering users, or checking out books.

Future Enhancements

    Implement additional features such as fine management, admin privileges, and advanced search capabilities.
    Enhance the frontend with a graphical user interface (GUI) for better user interaction.

Contributors

    Alpenglow42 - Sole contributor and developer.

License

This project is licensed under the MIT License - see the LICENSE file for details.
