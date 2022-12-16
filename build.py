from datetime import datetime
import json
import logging
from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine, select, func, update, text
from sqlalchemy.orm import Session

from Models.Base import Base
from Models.Library import Library
from Models.AllTime import AllTime
from Models.Library import Library
from Setup.constants import LIBRARIES
from Setup.setup import main as getData

'''
Only for initializing database for API
'''

def main():
    load_dotenv()
    # initialize connection to database
    engine = create_engine(getenv("DB"))
    session = Session(bind=engine, autoflush=False)

    # Drop tables if exist
    try:
        stmt = text("DROP TABLE IF EXISTS alltime, library CASCADE;")
        # session.query(AllTime).delete()
        # session.query(Library).delete()
        engine.execute(stmt)
    except:
        session.rollback()

    # Build database
    Base.metadata.create_all(engine, checkfirst=True)

    library_data = []
    for lib in LIBRARIES:
        item = Library(lib)
        library_data.append(item)
    session.add_all(library_data)

    # Fetching data
    data = getData()
    # Prepare data for database
    all_time_data = []
    for d in data:
        item = AllTime(d)
        all_time_data.append(item)
    session.add_all(all_time_data)
    
    session.commit() # insert into database

if __name__ == "__main__":
    main()