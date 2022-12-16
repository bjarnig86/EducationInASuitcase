from typing import Union
from fastapi import FastAPI

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from Models.Library import Library
from Models.AllTime import AllTime
from Models.History import History
from Models.Base import Base

'''
-- Libraries (AllTime) --
R   GET /library/{id}
L   GET /libraries --PARAMS

-- History --
R   GET /library/history/{lib_id}
U   UPDATE /library/history/{lib_id}
D   DELETE /library/history/{lib_id}
L   GET /libraries/history --PARAMS
'''

app = FastAPI()

engine = create_engine("postgresql+psycopg2://localhost:5432/smileylibs?user=postgres&password=12345")
Base.metadata.create_all(engine)
session = Session(bind=engine, autoflush=False)

@app.get("/")
def home():
    return {"message": "Welcome to SmileyCoin API"}

@app.get("/libraries")
def get_libraries():
    res = session.query(AllTime).join(Library.short_name == AllTime.name, full=True)
    return res
