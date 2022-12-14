from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from os import getenv
from dotenv import load_dotenv
from deta import App
from Models.Base import Base
from program import cron



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

app = App(FastAPI())

load_dotenv()
engine = create_engine(getenv("DB"))
Base.metadata.create_all(engine)

# -- HOME --
@app.get("/")
def home():
    return RedirectResponse("/docs")

# -- Library routes --
@app.get("/libraries")
def list_libraries():
    with Session(bind=engine, autoflush=False):
        try:
            stmt = text("SELECT * FROM alltime full outer join library on alltime.name = library.short_name;")
            res = engine.execute(stmt).all()
            if not res:
                return status.HTTP_404_NOT_FOUND
        except:
            return status.HTTP_500_INTERNAL_SERVER_ERROR
        return res

@app.get("/libraries/{lib_name}")
def read_library(lib_name):
    with Session(bind=engine, autoflush=False):
        try:
            stmt = text("SELECT * FROM alltime full outer JOIN library on alltime.name = library.short_name WHERE alltime.name = :name")
            res = engine.execute(stmt, name=lib_name).first()
            if not res:
                return status.HTTP_404_NOT_FOUND
        except:
            return status.HTTP_500_INTERNAL_SERVER_ERROR
        return res

# -- History routes --
@app.get('/history')
def list_library_history():
    with Session(bind=engine, autoflush=False):
        try:    
            stmt = text("SELECT * FROM history join library on history.name = library.short_name;")
            res = engine.execute(stmt).all()
            if not res:
                return status.HTTP_404_NOT_FOUND
        except:
            return status.HTTP_500_INTERNAL_SERVER_ERROR
        return res

@app.get('/history/{lib_name}')
def read_library_history(lib_name):
    with Session(bind=engine, autoflush=False):
        try:
            stmt = text("SELECT * FROM history JOIN library on history.name = library.short_name WHERE history.name = :name")
            res = engine.execute(stmt, name=lib_name).first()
            if not res:
                return status.HTTP_404_NOT_FOUND
        except:
            return status.HTTP_500_INTERNAL_SERVER_ERROR
        return res


@app.get('/manual-cron')
def manual_cron_job():
    with Session(bind=engine, autoflush=False):
        try:
            cron()
        except:
            return {"message": "Manual Cron Job failed!"}
    return {"message": "Manual Cron Job SUCCESSFUL"}

# @app.lib.cron()
# def cron_cron(event):
#     cron()
#     return "Cron Execution Completed 2.0"

@app.lib.cron()
def cron_job(event = None):
    cron()
    return "Cron Execution Completed"
