from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Practice API", version="1.0.0")


class Item(BaseModel):
    name: str
    price: float = 0.0
    is_available: bool = True


items = [
    {"id": 1, "name": "Laptop", "price": 999.99, "is_available": True},
    {"id": 2, "name": "Mouse", "price": 29.99, "is_available": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


@app.get("/items")
def get_items():
    return {"items": items}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}


@app.post("/items")
def create_item(item: Item):
    new_item = {
        "id": len(items) + 1,
        "name": item.name,
        "price": item.price,
        "is_available": item.is_available,
    }
    items.append(new_item)
    return new_item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("p:app", host="0.0.0.0", port=8000, reload=True)
