# set up and dependencies
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date
from sqlalchemy.orm import Session
from sqlalchemy import func
from flask import Flask, jsonify, request

#set up base
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

# create engine and session to link to the database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()
session = Session(bind=engine)

# establish app
app = Flask(__name__)

# create home page route
@app.route("/")
def main():
    return (
        f"Welcome to the Climate App Home Page!<br>"
        f"Available Routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start>/<end><br>"
    )

# create precipitation route of last 12 months of precipitation data
@app.route("/api/v1.0/precipitation")
def precip():

    recent_prcp = session.query(str(Measurement.date), Measurement.prcp)\
    .filter(Measurement.date > '2016-08-22')\
    .filter(Measurement.date <= '2017-08-23')\
    .order_by(Measurement.date).all()

    # convert results to a dictionary with date as key and prcp as value
    prcp_dict = dict(recent_prcp)

    #return json list of dictionary
    return jsonify(prcp_dict)


# create station route of a list of the stations in the dataset


# create tobs route of temp observations for most active station over last 12 months


# create start and start/end route
# min, average, and max temps for a given start or start-end range

if __name__ == "__main__":
    app.run(debug=True)