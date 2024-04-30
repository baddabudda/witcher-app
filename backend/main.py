from typing import Annotated
from fastapi import FastAPI, HTTPException, Depends, Body, status
from pydantic import BaseModel

from database import engine, SessionLocal
import models

from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("UI_HOST"),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

class CountBase(BaseModel):
    value: int

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/")
async def edit_count_value(db: db_dependency, action: str = Body()):
    summand = 0

    if action == "toss": summand = 1
    elif action == "steal": summand = -1

    db.query(models.Count) \
        .filter(models.Count.id == 1) \
        .update({models.Count.value: models.Count.value + summand})
    db.commit()

    count = db.query(models.Count) \
                .filter(models.Count.id == 1)\
                .first()

    return count.value

@app.get("/")
async def read_count(db: db_dependency):
    count = db.query(models.Count) \
                .filter(models.Count.id == 1)\
                .first()
    
    if count is None:
        raise HTTPException(status_code=500, detail="No rows found")
    return count.value

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}