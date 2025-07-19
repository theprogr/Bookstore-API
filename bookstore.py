from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

book_store = [{"title": "Peter Pan", "author": "J.M Barrie", "price": 4, "in_stock": True, "rating": 4.7, "id": 1}]

class Book(BaseModel):
    title: str
    author: str
    price: float
    in_stock: bool = True
    rating: Optional[float]


@app.get("/books")
def view_books():
    return {"Books": book_store}


@app.get("/books/latest")
def get_latest_book():
    latest_book = book_store[len(book_store) - 1]
    return {"Latest book": latest_book}


@app.get("/books/in-stock")
def books_in_stock():
    res = []
    for book in book_store:
        if book["in_stock"]:
            res.append(book)
    return {"Books in stock": res}


@app.get("/books/{id}")
def get_book(id: int):
    for book in book_store:
        if book['id'] == id:
            return {"Book": book}
    raise HTTPException(status_code=404, detail="Book with an id of {id} was not found!")


@app.post("/books", status_code=status.HTTP_201_CREATED)
def add_book(book: Book):
    book_dict = book.model_dump() # model -> dictionary
    book_dict['id'] = randrange(1, 1000000)     
    book_store.append(book_dict)  # storing in array
    return {"data": book_dict}


@app.put("/books/{id}")
def update_info(id: int, book: Book):
    for index, item in enumerate(book_store):
        if item['id'] == id:
            book_dict = book.model_dump()
            book_dict['id'] = id
            book_store[index] = book_dict
            return {"Updated book": book_dict}
    raise HTTPException(status_code=404, detail="Book with an id of {id} was not found!")


@app.delete("/books/{id}")
def remove_book(id: int):
    for index, item in enumerate(book_store):
        if item['id'] == id:
            book_store.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail="Book with an id of {id} was not found!")