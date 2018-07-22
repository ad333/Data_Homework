from flask import Flask, render_template, jsonify, request

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc, select

import datetime as dt
import numpy as np
import pandas as pd

# Database Setup
engine = create_engine("sqlite:///DataSets/belly_button_biodiversity.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

# Save reference to the table
Otu = Base.classes.otu
Samples = Base.classes.samples
Samples_metadata = Base.classes.samples_metadata

# Create session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/names")  
def names():
    results = session.query(Samples_metadata.SAMPLEID).all()
    
    sample_id = []
    for i in results:
        sample_id.append('BB_' + str(i[0]))
    return jsonify(sample_id)
    

@app.route("/otu")   
def otu():
    results = session.query(Otu.lowest_taxonomic_unit_found).all()

    otu_descriptions = []
    for i in results:
        otu_descriptions.append(i[0])
    return jsonify(otu_descriptions)

@app.route("/metadata/<sample>")  
def metadata(sample):
    sampleID_short = int(sample.replace("BB_", ""))
    
    #results = session.query(Samples_metadata.AGE, Samples_metadata.BBTYPE, Samples_metadata.ETHNICITY, Samples_metadata.GENDER, Samples_metadata.LOCATION, Samples_metadata.SAMPLEID).  \
    #          filter(Samples_metadata.SAMPLEID == sampleID_short).all()

    results = session.query(Samples_metadata).all()

    results_dict = {}
    
    for i in results:
        if (sampleID_short == i.SAMPLEID):
            results_dict["AGE"] = i.AGE
            results_dict["BBTYPE"] = i.BBTYPE
            results_dict["ETHNICITY"] = i.ETHNICITY
            results_dict["GENDER"] = i.GENDER
            results_dict["LOCATION"] = i.LOCATION
            results_dict["SAMPLEID"] = i.SAMPLEID

    return jsonify(results_dict)

@app.route("/wfreq/<sample>")  
def weekly_freq(sample):
    sampleID_short = int(sample.replace("BB_", ""))
    
    results = session.query(Samples_metadata).all()

    weekly_frequency = {}

    for i in results:
        if (sampleID_short == i.SAMPLEID):
            weekly_frequency["WFREQ"] = i.WFREQ

    return jsonify(weekly_frequency)        


@app.route('/samples/<sample>')
def samplesData(sample):
    #results = pd.read_csv("DataSets/belly_button_biodiversity_samples.csv")
    #results_dict = results.to_dict(orient = "list")
    #return jsonify(results_dict)

    results = session.query(Samples.otu_id, sample).order_by(desc(sample))

    sample_dict = {}
    otu_ids = []
    sample_values = []

    for i in results:
        otu_ids.append(i[0])
        sample_values.append(i[1])

    sample_dict = {"otu_ids":otu_ids, "sample_values":sample_values}   

    return jsonify(sample_dict) 

if __name__ == "__main__":
    app.run(debug=True)