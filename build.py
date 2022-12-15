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
from Models.Library import Library
from Setup.constants import LIBRARIES
from Setup.setup import main as getData
from progress_bar import progress_bar

'''
Only for initializing database for API
'''

def main():
    # initialize connection to database
    engine = create_engine("postgresql+psycopg2://localhost:5432/smileylibs?user=postgres&password=12345")
    Base.metadata.create_all(engine, checkfirst=True)
    session = Session(bind=engine, autoflush=False)

    # Fetching data
    data = getData()
    # Prepare data for database
    all_time_data = []
    for d in data:
        item = AllTime(d)
        all_time_data.append(item)
    session.add_all(all_time_data)
    
    library_data = []
    for lib in LIBRARIES:
        item = Library(lib)
        library_data.append(item)
    session.add_all(library_data)
    
    session.commit() # insert into database

if __name__ == "__main__":
    main()