from datetime import datetime
import json
import logging
from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine, select, func, update
from sqlalchemy.orm import Session
from sqlalchemy.engine import URL
from sqlalchemy.engine import URL
from sqlalchemy.exc import DatabaseError
from timeit import default_timer as timer

from Models.Base import Base
from Models.AllTime import AllTime
from Models.History import History
from Models.Library import Library

from Setup.setup import main as getData

load_dotenv()

# initialize connection to database
engine = create_engine(getenv("DB"))
Base.metadata.create_all(engine)
session = Session(bind=engine, autoflush=False)

# Fetching new and old data
curr = getData()
stmt = select(AllTime)
prev = session.execute(stmt).all()

## Check if there is any difference between current data and previous data.
historical_changes = False
for i in range(len(curr)):
    changes_in_row = {"name": curr[i]["name"]}
    for key in curr[i].keys():
        same = curr[i][key] == (getattr(prev[i][0], key)) 
        if not same:
            print(curr[i][key], "-" ,getattr(prev[i][0], key))
            changes_in_row[key] = curr[i][key] - getattr(prev[i][0], key)
            
    if len(changes_in_row) > 1:
        historical_changes = True
        new_row = History(changes_in_row)
        session.add(new_row)

if historical_changes:
    AllTime.__table__.drop(engine)
    Base.metadata.create_all(engine)

    alles = []
    for b in getData():
        item = AllTime(b)
        alles.append(item)

    stmt = select(AllTime)
    if not session.execute(stmt).first():
        session.add_all(alles)

session.commit()
    

