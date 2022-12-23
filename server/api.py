from fastapi import FastAPI
from pydantic import BaseModel
from .parser import extract_from_html

class Item(BaseModel):
    body: str

app = FastAPI()


@app.post("/parse")
async def parse(item: Item):
    body = extract_from_html(item.body)

    return {"data": body}

