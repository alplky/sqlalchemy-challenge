# set up and dependencies

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date
from sqlalchemy.orm import Session
from sqlalchemy import func
import pandas as pd 
from pprint import pprint

# set up Base

Base = declarative_base()

#create class for measurement table

class Measurement(Base):
    __tablename__ = "measurement"
    
    id = Column(Integer, primary_key=True)
    station = Column(String)
    date = Column(Date)
    prcp = Column(Float)
    tobs = Column(Float)
    
#create class for station table

class Station(Base):
    __tablename__ = "station"
    
    id = Column(Integer, primary_key=True)
    station = Column(String)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation =  Column(Float)
    
# create an engine and session to link to the database

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()
session = Session(bind=engine)

# look at first 10 of measurement table

measurement_rows = session.query(Measurement).limit(10)

# for row in measurement_rows:
#     pprint(row.__dict__)

# get the last 12 months of precipitation data

#check the max date in data
max_date = session.query(func.max(Measurement.date)).first()[0]
# print(max_date)
# max date is 2017-08-23

# get the last 12 months of precipitation data

recent_prcp = session.query(Measurement.date, func.round(func.sum(Measurement.prcp), 2)).filter(Measurement.date > '2016-08-23').filter(Measurement.date <= '2017-08-23').group_by(Measurement.date).order_by(Measurement.date).all()

# load query results into a Pandas dataframe

prcp_df = pd.DataFrame(recent_prcp, columns = ["Date", "Rain in Inches"])

print(prcp_df)