from fastapi import FastAPI
from typing import Union, Annotated # types
from pydantic import BaseModel # A base class for creating Pydantic models, for validation and schema definition.
from enum import Enum # Enum base class

app = FastAPI()

class ItemType (str, Enum):
    FOOD = "food"
    TOY = "toy"
    ELECTRONICS = "electronics"

class Item(BaseModel):
    id: Annotated[int | None, "ID of the item"] = None # Optional integer field
    name: str
    price: float
    is_offer: Union[bool, None] = None # Union[str, None] means that q can be a string or None
    type: ItemType
    

items: list[Item] = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(
    item_id: int,  #item_id is path, validates with integer
    skip: int = 0,  #skip is query, validates with integer
    limit: int = 10,  #limit is query, validates with integer
    allRecords: bool | None = None  #allRecords is query, validates with boolean
    ):
    print(skip, limit, allRecords)
    return next((item for item in items if item.id == item_id), None)

@app.post("/items/")
def create_item(item: Item):
    item.id = len(items) + 1
    items.append(item)
    if(item.type is ItemType.FOOD): # if using at is, use EnumClass.Member
        print("This is a food item.")
    if(item.type.value == "food"): # if using eqeq, use .value and string
        print("This is a food item.")
    return item

@app.get("/path/{item_id:path}") # now we can pass values like /path/some/longer/path/here
def pathDefinition(item_id: str): # item_id is path, validates with in, q is query, optional
    return {"item_id": item_id}