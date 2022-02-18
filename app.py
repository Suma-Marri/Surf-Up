# Import Python dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask dependency
from flask import Flask

# Access the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create the classes variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to the database
session = Session(engine)

# Use magic method __name__ to check file source of running code
import app
print("example __name__ = %s", __name__)

if __name__ == "__main__":
	print("example is being run directly.")
else:
	print("example is being imported")

# Define the Flask app
app = Flask(__name__)

# Define the welcome route
@app.route("/")

# Add the routing information for each of the other routes
def welcome():
	return(
	'''
	Welcome to the Climate Analysis API!
	Available Routes:
	/api/v1.0/precipitation
	/api/v1.0/stations
	/api/v1.0/tobs
	/api/v1.0/temp/start/end
	''')