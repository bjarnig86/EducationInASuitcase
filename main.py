from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from sqlalchemy import create_engine, select, join, outerjoin, text
from sqlalchemy.orm import Session

from Models.Library import Library
from Models.AllTime import AllTime
from Models.History import History
from Models.Base import Base

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
    stmt = text("SELECT * FROM library NATURAL JOIN alltime;")
    res = engine.execute(stmt).all()
    return res

@app.get("/libraries/{lib_id}")
def read_library():
    res = session.query(AllTime) # sem sækir úr AllTime eftir ID (og joinar Library)
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
