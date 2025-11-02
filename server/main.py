from fastapi import FastAPI, Query
from typing import Union, Annotated, Literal # types
from pydantic import BaseModel # A base class for creating Pydantic models, for validation and schema definition.
from enum import Enum # Enum base class
from datetime import datetime, time, timedelta

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
    created_at: str
    
class User(BaseModel):
    username: str
    full_name: str | None = None
    
class Filter(BaseModel):
    order_by: Literal['created_at'] = 'created_at'
    order: Literal['asc', 'desc'] = 'asc'

items: list[Item] = []
users: list[User] = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(
    filters: Annotated[Filter, Query()],
    item_id: int,  #item_id is path, validates with integer
    skip: int = 0,  #skip is query, validates with integer
    limit: int = 10,  #limit is query, validates with integer
    allRecords: bool | None = None,  #allRecords is query, validates with boolean
    search: Annotated[str | None, Query(max_length=50)] = None, # search is query, validates with string max length 50
    types: Annotated[list[ItemType] | None, Query()] = None, # list of enum values, passed as type=Food&type=Toy
    ):
    print(skip, limit, allRecords, search, types.__str__(), filters) 
    return (item for item in items if item.id == item_id)

@app.get("/items")
def read_items(filters: Annotated[Filter, Query()]):
    return filters

@app.post("/items/")
def create_item(item: Item, user: User):
    item.id = len(items) + 1
    item.created_at = datetime.now().isoformat()
    items.append(item)
    users.append(user)
    if(item.type is ItemType.FOOD): # if using at is, use EnumClass.Member
        print("This is a food item.")
    if(item.type.value == "food"): # if using eqeq, use .value and string
        print("This is a food item.")
    return item

@app.get("/path/{item_id:path}") # now we can pass values like /path/some/longer/path/here
def pathDefinition(item_id: str): # item_id is path, validates with in, q is query, optional
    return {"item_id": item_id}