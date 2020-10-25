# set up and dependencies
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime

#connect to database
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Resources/hawaii.sqlite"

db = SQLAlchemy(app)

#create class for measurement table

class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String(15))
    date = db.Column(db.Date)
    prcp = db.Column(db.Float)
    tobs = db.Column(db.Float)

    #convert class to dict
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(
                getattr(self, column.name), (datetime.datetime, datetime.date)
            )
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }

#create class for station table

class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String(15))
    name = db.Column(db.String(45))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    elevation =  db.Column(db.Float)

    #convert class to dict
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(
                getattr(self, column.name), (datetime.datetime, datetime.date)
            )
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }

# create specified tables
db.create_all()

# create home page route
@app.route("/")
def main():
    return (
        f"Welcome to the Climate App Home Page!<br>"
        f"Available Routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start><br>"
        f"/api/v1.0/<start>/<end><br>"
    )

if __name__ == "__main__":
    app.run(debug=True)