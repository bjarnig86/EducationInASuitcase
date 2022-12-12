from datetime import datetime
import json
import logging
from sqlalchemy import create_engine, select, func, update
from sqlalchemy.orm import Session
from sqlalchemy.engine import URL
from sqlalchemy.exc import DatabaseError
from timeit import default_timer as timer

from Models.Base import Base
from Models.AllTime import AllTime
from Models.History import History
from Models.Library import Library

# initialize connection to database

engine = create_engine("postgresql+psycopg2://localhost:5432/smileylibs?user=postgres&password=12345")
Base.metadata.create_all(engine, checkfirst=True)

session = Session(bind=engine, autoflush=False)

