from fastapi import FastAPI
from typing import Union # types
from pydantic import BaseModel # A base class for creating Pydantic models.

app = FastAPI()

class Item(BaseModel):
    id: int | None = None # Optional integer field
    name: str
    price: float
    is_offer: Union[bool, None] = None # Union[str, None] means that q can be a string or None

items: list[Item] = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None): # item_id is path, validates with in, q is query, optional
    return next((item for item in items if item.id == item_id), None)

@app.post("/items/")
def create_item(item: Item):
    item.id = len(items) + 1
    items.append(item)
    return item