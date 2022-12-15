from typing import Union
from fastapi import FastAPI

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from Models.AllTime import AllTime
from Models.Base import Base
from Models.History import History
from Models.Library import Library

app = FastAPI()

engine = create_engine("postgresql+psycopg2://localhost:5432/smileylibs?user=postgres&password=12345")
Base.metadata.create_all(engine)
session = Session(bind=engine, autoflush=False)

@app.get("/")
def home():
    return {"message": "Welcome to SmileyCoin API"}

@app.get("/libraries")
def get_libraries():
    stmt = select(AllTime)
    res = engine.execute(stmt).all()
    return res
