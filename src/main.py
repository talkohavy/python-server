"""This is the entry file"""

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_books():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def get_single_book(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# run it with: fastapi dev src/main.py
