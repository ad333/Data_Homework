import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurements = Base.classes.measurements
Stations = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/end<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a json dictionary of the date and observation from last year"""
    # Query for date and temperature observation
    results = session.query(Measurements.date, Measurements.tobs).  \
              filter(Measurements.date >= '2017, 1, 1').  \
              filter(Measurements.date < '2018, 1, 1').  \
              order_by(Measurements.date).all()

    # Convert the query results to dictionary
    prec = []
    for i in results:
        prec_dict = {}
        prec_dict['Date'] = Measurements.date
        prec_dict['Tobs'] = Measurements.tobs
        prec.append(prec_dict)
    return jsonify(prec)    

@app.route("/api/v1.0/stations")
def stations():
    """Return a json list of stations from the dataset"""
    # Query
    results = session.query(Stations.station).all()

    # Convert results to list and return as json
    stations_list = list(np.ravel(results))
    return jsonify(stations_list)


@app.route("/api/v1.0/tobs")
def tobs():
    """Return a json list of Temperature Observations (tobs) for the previous year"""
    # Query
    results = session.query(Measurements.tobs).  \
              filter(Measurements.date >= '2017, 1, 1').  \
              filter(Measurements.date < '2018, 1, 1').all()
    
    # # Convert results to list and return as json
    tobs_list = list(np.ravel(results))
    return jsonify(tobs_list)


@app.route("/api/v1.0/<start>")
def start_(start):
    start_date= dt.datetime.strptime(start, '%Y-%m-%d')
    last_year = dt.timedelta(days=365)
    start = start_date-last_year
    end =  dt.date(2017, 8, 23)
    
    # Query
    results = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
                filter(Measurements.date >= start).filter(Measurements.date <= end).all()
    
    # Convert results to list and return as json
    data = list(np.ravel(results))
    return jsonify(data)


@app.route("/api/v1.0/<start>/<end>")
def startend(start, end):
    start_date= dt.datetime.strptime(start, '%Y-%m-%d')
    end_date= dt.datetime.strptime(end,'%Y-%m-%d')
    last_year = dt.timedelta(days=365)
    start = start_date-last_year
    end = end_date-last_year
    
    # Query
    results = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start).filter(Measurements.date <= end).all()
    
    # Convert to list and return as json
    data = list(np.ravel(results))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)