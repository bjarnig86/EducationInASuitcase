from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from sqlalchemy import create_engine, select, join, outerjoin, text
from sqlalchemy.orm import Session

from Models.Library import Library
from Models.AllTime import AllTime
from Models.History import History
from Models.Base import Base

NATURAL = "NATURAL JOIN library"

'''
-- Libraries (AllTime) --
R   GET /libraries/{id}
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

# -- HOME --
@app.get("/")
def home():
    return RedirectResponse("/docs")

# -- Library routes --
@app.get("/libraries")
def list_libraries():
    stmt = text("SELECT * FROM alltime NATURAL JOIN library;")
    res = engine.execute(stmt).all()
    return res

@app.get("/libraries/{lib_name}")
def read_library(lib_name):
    stmt = text("SELECT * FROM alltime WHERE name = :s NATURAL JOIN library")
    # stmt = select(AllTime).where(AllTime.name == lib_name).join()
    res = engine.execute(stmt, s=lib_name).fetchall()
    return res

# -- History routes --
@app.get('/libraries/history/{lib_id}')
def read_library_history():
    pass

@app.patch('/libraries/history/{lib_id}')
def update_library_history():
    pass

@app.delete('/libraries/history/{lib_id}')
def delete_library_history():
    pass

@app.get('/libraries/history')
def list_library_history():
    pass
