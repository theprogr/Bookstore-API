📚 Simple Bookstore API – FastAPI Project
This is a CRUD-style RESTful API for a digital bookstore, built using FastAPI and Pydantic.
The API allows users to manage a collection of books — including creating, reading, updating, and deleting book records — all stored in-memory using Python data structures.

🚀 Features
✅ View all books

✅ Retrieve a book by ID

✅ Create a new book

✅ Update existing book info

✅ Delete a book

✅ View the latest added book

✅ Filter books that are in stock

📦 Book Data Model
Each book contains the following fields:

title (string): Required

author (string): Required

price (float): Required

in_stock (bool): Optional, defaults to True

rating (float): Optional

id (int): Auto-generated
