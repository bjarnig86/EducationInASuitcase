from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from os import getenv
from dotenv import load_dotenv

from Models.Base import Base

'''
-- Libraries (AllTime) --
C   X
R   GET /libraries/{id}
U   X
D   X
L   GET /libraries --PARAMS

-- History --
C   X
R   GET /library/history/{lib_id}
U   X
D   X
L   GET /libraries/history --PARAMS
'''

app = FastAPI()

load_dotenv()
engine = create_engine(getenv("DB"))
Base.metadata.create_all(engine)
session = Session(bind=engine, autoflush=False)

# -- HOME --
@app.get("/")
def home():
    return RedirectResponse("/docs")

# -- Library routes --
@app.get("/libraries")
def list_libraries():
    stmt = text("SELECT * FROM alltime full outer join library on alltime.name = library.short_name;")
    res = engine.execute(stmt).all()
    return res

@app.get("/libraries/{lib_name}")
def read_library(lib_name):
    stmt = text("SELECT * FROM alltime full outer JOIN library on alltime.name = library.short_name WHERE alltime.name = :name")
    res = engine.execute(stmt, name=lib_name).first()
    return res

# -- History routes --
@app.get('/history')
def list_library_history():
    stmt = text("SELECT * FROM history join library on history.name = library.short_name;")
    res = engine.execute(stmt).all()
    return res

@app.get('/history/{lib_name}')
def read_library_history(lib_name):
    stmt = text("SELECT * FROM history JOIN library on history.name = library.short_name WHERE history.name = :name")
    res = engine.execute(stmt, name=lib_name).first()
    return res
