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

from Setup.setup import main as getData

# initialize connection to database

engine = create_engine("postgresql+psycopg2://localhost:5432/smileylibs?user=postgres&password=12345")
Base.metadata.create_all(engine, checkfirst=True)

session = Session(bind=engine, autoflush=False)

# ble = getData()


# alles = []
# for b in ble:
#     item = AllTime(b)
#     alles.append(item)

# stmt = select(AllTime)
# if not session.execute(stmt).first():
#     session.add_all(alles)
#     session.commit()

curr = getData()
stmt = select(AllTime)
prev = session.execute(stmt).all()

for i in range(len(curr)):
    print("i", i)
    for item in curr[i].keys():
        same = str(curr[i][item]) == (str(getattr(prev[i][0], item)))
        if not same:
            print(curr[i][item], " is not the same as ", str(getattr(prev[i][0], item)))
            print(type(curr[i][item]), " is not the same as ", type(str(getattr(prev[i][0], item))))

# for i in range(len(curr)):
#     print(curr[i]["name"])
#     print("___________________")
#     if curr[i]["name"] != str(prev[i][0].name):
#         print("name",type( curr[i]["name"]), type(prev[i][0].name))
#     if curr[i]["total_mill_smileys"] != str(prev[i][0].total_mill_smileys):
#         print("total_mill_smileys",type(curr[i]["total_mill_smileys"]), type(prev[i][0].total_mill_smileys))
#     if curr[i]["no_mill_smiley_earned"] != str(prev[i][0].no_mill_smiley_earned):
#         print("no_mill_smiley_earned",type(curr[i]["no_mill_smiley_earned"]), type(prev[i][0].no_mill_smiley_earned))
#     if curr[i]["active"] != str(prev[i][0].active):
#         print("active",type(curr[i]["active"]), type(prev[i][0].active))
#     if curr[i]["issued_qr"] != str(prev[i][0].issued_qr):
#         print("issued_qr",type(curr[i]["issued_qr"]), type(prev[i][0].issued_qr))
#     if curr[i]["sold_tablets"] != str(prev[i][0].sold_tablets):
#         print("sold_tablets",type(curr[i]["sold_tablets"]), type(prev[i][0].sold_tablets))
#     if curr[i]["no_accounts"] != str(prev[i][0].no_accounts):
#         print("no_accounts",type(curr[i]["no_accounts"]), type(prev[i][0].no_accounts))
#     if curr[i]["no_delivered_tablets"] != str(prev[i][0].no_delivered_tablets):
#         print("no_delivered_tablets",type(curr[i]["no_delivered_tablets"]), type(prev[i][0].no_delivered_tablets))
#     if curr[i]["no1m_acc_rate"] != str(prev[i][0].no1m_acc_rate):
#         print("no1m_acc_rate",type(curr[i]["no1m_acc_rate"]), type(prev[i][0].no1m_acc_rate))
#     if curr[i]["sold_delivered_rate"] != str(prev[i][0].sold_delivered_rate):
#         print("sold_delivered_rate",type(curr[i]["sold_delivered_rate"]), type(prev[i][0].sold_delivered_rate))
#     if curr[i]["avail_tablets"] != str(prev[i][0].avail_tablets):
#         print("avail_tablets",type(curr[i]["avail_tablets"]), type(prev[i][0].avail_tablets))
#     if curr[i]["unused_accounts"] != str(prev[i][0].unused_accounts):
#         print("unused_accounts",type(curr[i]["unused_accounts"]), type(prev[i][0].unused_accounts))
#     if curr[i]["no_kcse_complete"] != str(prev[i][0].no_kcse_complete):
#         print("no_kcse_complete",type(curr[i]["no_kcse_complete"]), type(prev[i][0].no_kcse_complete))
#     print("______________________________")






