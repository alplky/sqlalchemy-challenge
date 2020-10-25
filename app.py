# set up and dependencies
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime

#connect to database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Resources/hawaii.sqlite"

db = SQLAlchemy(app)

#create class for measurement table

class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String(15))
    date = db.Column(db.Date)
    prcp = db.Column(db.Float)
    tobs = db.Column(db.Float)

#create class for station table

class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String(15))
    name = db.Column(db.String(45))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    elevation =  db.Column(db.Float)

