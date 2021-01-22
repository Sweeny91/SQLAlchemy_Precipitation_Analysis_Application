# Dependencies
import pandas as pd
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, insepct

from flask import Flask, jsonify

# Prepare Database Path, Engine, and Base
engine = create_engine("sqlite:///Instructions/Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Database tables
measurements = Base.classes.measurement
stations = Base.classes.station 

# App info
app = Flask(__name__)

# Routes
# Home Page
@app.route("/")
def welcome():
    return (
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        " - This route shows a list of precipitation by each day<br/>"
        "/api/v1.0/stationlist<br/>"
        " - This route shows a list of all the weather stations<br/>"
        "/api/v1.0/tobs<br/>"
        " - This route shows all temperature information<br/>"
        "/api/1.0/start<br/>"
        " - This route shows the minimum, max, and mean temperatures of all dates GREATER than the date entered<br/>"
        " - Please enter the date in format: yyyy-mm-dd<br/>"
        "/api/v1.0/start/end<br/>"
        " - This route shows the minimum, max, and mean temperatures for all dates BETWEEN the START and END dated entered<br/>"
        " - Please enter the date in format: (start/end) 'yyyy-mm-dd/yyyy-mm-dd'<br/>"
    )


# Precipitation
# Convert the query results to a dictionary using {date : prcp} as the {key : value}.
# Return the dictionary of your data in JSON format.

@app.route("/api/v1.0/precipitation/")
def precipitation():
    session = Session(engine)
    results = session.query(measurements.date, measurements.prcp).all()

    prcp_data = []
    for date, prcp in results:
        dict_data = {}
        dict_data[date] = prcp
        prcp_data.append(dict_data)

    session.close()
    
    return jsonify(prcp_data)

# Station List
# Return a list of stations from the dataset in JSON format.

@app.route("/api/v1.0/stationlist/")
def stationlist():
    session = Session(engine)
    results = session.query(stations.station, stations.name).all()
    station_data = {}
    for station, name in results:
        station_data[station] = name

    session.close()

    return jsonify(station_data)

# TOBS
# Query the dates and temperature observations of the most active station for the last year of data.
# Return a list of temperature observations in JSON format.

@app.route("/api/v1.0/tobs/")
def tobs():
    session = Session(engine)

    most_recent_date = session.query(measurements.date).order_by(measurements.date.desc()).first()
    year_start_date = (dt.datetime.strptime(most_recent_date[0],'%Y-%m-%d')-dt.timedelta(days=365)).strftime('%Y-%m-%d')

    results = session.query(measurements.date, measurements.tobs).filter(measurements.date >= year_start_date).order_by(measurements.date).all()

    date_data = []
    for date, tobs in results:
        dict_data = {}
        dict_data[date] = tobs
        date_data.append(dict_data)

    session.close()

    return jsonify(date_data)

# Start-End
# Return a list of the minimum temperature, the average temperature, and the max temperature for a given start-end range in JSON format
# When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

@app.route("/api/v1.0/<start>")
def start_date(start):
    session = Session(engine)

    results = session.query(func.min(measurements.tobs), func.avg(measurements.tobs), func.max(measurements.tobs)).filter(measurements.date >= start).all()

    tobs_data = []
    for min, avg, max in results:
        tobs_dict = {}
        tobs_dict["min"] = min
        tobs_dict["mean"] = avg
        tobs_dict["max"] = max

    session.close()

    return jsonify(tobs_dict)

# Given the start and end dates, calculate the TMIN, TAVG, and TMAX for dates between them, including the end date.

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    session = Session(engine)

    results = session.query(func.min(measurements.tobs), func.avg(measurements.tobs), func.max(measurements.tobs)).filter(measurements.date >= start).filter(measurements.date <= end).all()

    tobs_data = []
    for min, avg, max in results:
        tobs_dict = {}
        tobs_dict["min"] = min
        tobs_dict["mean"] = avg
        tobs_dict["max"] = max
        
    session.close()

    return jsonify(tobs_dict)


# Debug control

if __name__ == '__main__':
    app.run(debug=True)