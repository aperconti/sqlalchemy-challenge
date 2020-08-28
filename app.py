import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
measurement = Base.classes.measurement
station = Base.classes.station

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
        f"Aloha! Here are some links so you can explore the local weather.<br/>"
        f"<a href='/api/v1.0/stations'> List of Stations </a><br/>"
        f"<a href='/api/v1.0/precipitation'> Daily precipitation </a><br/>"
        f"<a href='/api/v1.0/tobs'> Temperature observation data </a><br/>"
        f"<a href='/api/v1.0/<start>/<end>'> Temperature infomation for chosen vacation </a><br/>"

    )
    
@app.route("/api/v1.0/stations")
def station_list():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all station names in station
    results = session.query(station.name).group_by(station.name).all()


    session.close()

    # Convert list of tuples into normal list
    all_results = list(np.ravel(results))

    return jsonify(all_results)




@app.route("/api/v1.0/precipitation")
def daily_precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query measurement for tobs and date 
    results = session.query(measurement.date, measurement.prcp).group_by(measurement.date).order_by(measurement.date.desc()).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_results
    all_results = []
    for item in results:
        item_dict = {}
        item_dict["date"] = item[0]
        item_dict["prcp"] = item[1]
        all_results.append(item_dict)

    return jsonify(all_results)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all countries in billing history
    results = session.query(station.name,measurement.date, measurement.tobs).filter(station.name == 'WAIKIKI 717.2, HI US').filter(measurement.date > '2016-08-22').all()

    session.close()

    # Convert list of tuples into normal list
    all_results = list(np.ravel(results))

    return jsonify(all_results)



@app.route("/api/v1.0/<start>/<end>")
def calc_temps(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start).filter(measurement.date <= end).all()
    
    output = f'Minimum temperature for your chosen vacation days is: {results[0][0]}, Average temperature for your chosen vacation days is: {results[0][1]}, Max temperature for your chosen vacation days is: {results[0][2]}'

    session.close()

    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
