import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt
from dateutil.relativedelta import relativedelta


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")


# Reflect an existing database into a new model.
Base = automap_base()

# Reflect the tables.
Base.prepare(engine, reflect=True)

# Save reference to the tables.
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__,static_url_path='/Images/surfingdog.png')


#################################################
# Flask Routes
#################################################

# Set the home page,and List all routes that are available. For easy to use I hyperlink the list

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<h1>Welcome to the Surfing Climate App API!</h1>"
        f"This is a Flask API for Climate Analysis.<br/><br/>"
        f" <img width='800' src='https://www.surfertoday.com/images/stories/surfingdog.jpg'/ >"
        f"<h2>Here are the available routes:</h2>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/yyyy-mm-dd<br/>"
        f"T/api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/><br/>"
    
    
        f"<h2>Here are the hyperlinked routes:</h2>"
        f"<ol><li><a href=http://127.0.0.1:5000/api/v1.0/precipitation>"
        f"PRECIPITATION amounts for the last year of data available</a></li><br/><br/>"
        f"<li><a href=http://127.0.0.1:5000/api/v1.0/stations>"
        f"List of weather STATION information</a></li><br/><br/>"
        f"<li><a href=http://127.0.0.1:5000/api/v1.0/tobs>"
        f"TEMPERATURES for the last year of data available</a></li><br/><br/>"
        f"<li><a href=http://127.0.0.1:5000//api/v1.0/yyyy-mm-dd>"
        f"Temperatures (min, avg, max) for a given START DATE (yyyy-mm-dd) through end date of available data</a></li><br/><br/>"
        f"<li><a href=http://127.0.0.1:5000//api/v1.0/yyyy-mm-dd/yyyy-mm-dd>"
        f"Temperatures (min, avg, max) between a given START and END DATE (yyyy-mm-dd)</a></li></ol><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
  
    # Find the most recent date in the data set
    last_date_string = session.query(Measurement.date).\
        order_by(Measurement.date.desc()).first()[0]
    
    # Calculate the date one year from the last date in data set.
    last_date = dt.datetime.strptime(last_date_string, '%Y-%m-%d')
    query_date = dt.date(last_date.year -1, last_date.month, last_date.day)
    
    # Query the database with date as the key and the value as the precipitation
    results = session.query(Measurement.date,Measurement.prcp).\
        filter(Measurement.date >= query_date).all()

    session.close()

    # Convert the query results to a dictionary 
    last_year_precip = []
    for date, prcp in results:
        if prcp != None:
            precip_dict = {}
            precip_dict[date] = prcp
            last_year_precip.append(precip_dict)

    # Return the JSON representation of dictionary
    return jsonify(last_year_precip)


@app.route("/api/v1.0/stations")
def stations():
    
    # Query the database for data of all stations in the database
    results = session.query(Station.station,Station.name,Station.latitude,
                            Station.longitude).all()

    session.close()

    # Convert the query results to a dictionary 
    stations = []
    for station, name, latitude, longitude in results:
        station_dict = {}
        station_dict["Station ID"] = station
        station_dict["Station Name"] = name
        station_dict["Latitude"] = latitude
        station_dict["Longitude"] = longitude
        stations.append(station_dict)

    # Return the JSON representation of dictionary
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    
    # Find the most recent date for temperature measurement for station USC00519281
    station_281_last_date_string = session.query(Measurement.date).\
        filter(Measurement.station == 'USC00519281').\
        order_by(Measurement.date.desc()).first()[0]# Calculate the date one year from the last temp measurement date for station USC00519281
    
    station_281_last_date = dt.datetime.strptime(station_281_last_date_string, '%Y-%m-%d')
    
    station_281_query_date = dt.date(station_281_last_date.year -1, station_281_last_date.month, station_281_last_date.day)

    # Perform a query to retrieve the date and temperatures scores for the last 12 months for station USC00519281
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').filter(Measurement.date >= station_281_query_date).all()
    
    session.close()

    # Convert the query results to a dictionary 
    last_year_temps = []
    for date, tobs  in results:
        if tobs != None:
            temps_dict = {}
            temps_dict[date] = tobs
            last_year_temps.append(temps_dict)

    # Return the JSON representation of dictionary
    return jsonify(last_year_temps)


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start=None, end=None):
    sel=[func.min(Measurement.tobs), func.round(func.avg(Measurement.tobs)), func.max(Measurement.tobs)]

    if not end:
        results=session.query(*sel).filter(Measurement.date>=start).all()
        session.close()

        temps_dates_1 = []
        for min,avg,max in results:
            tobs_dict_1 = {}
            tobs_dict_1["Min"] = min
            tobs_dict_1["Average"] = avg
            tobs_dict_1["Max"] = max
            temps_dates_1.append(tobs_dict_1)

        return jsonify(temps_dates_1)
    
    results=session.query(*sel).filter(Measurement.date>=start).filter(Measurement.date<=end).all()
    session.close()

    temps_dates_2 = []
    for min,avg,max in results:
        tobs_dict_2 = {}
        tobs_dict_2["Min"] = min
        tobs_dict_2["Average"] = avg
        tobs_dict_2["Max"] = max
        temps_dates_2.append(tobs_dict_2)

    return jsonify(temps_dates_2)

if __name__=='__main__':
    app.run()
    

