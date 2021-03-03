# sqlalchemy_challenge
All Tasks below were finished to completion. Bonus Analysis has not yet been submitted.
- Main script to be ran for analysis is "climate_analysis.ipynb"
- The climate app produced for part 2 can be found in "app.py"
- Note: original, unmodified starter files can be found in the instructions folder

## Step 1 - Climate Analysis and Exploration
- Began by, using Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
- Used the provided starter notebook and hawaii.sqlite files to complete the climate analysis and data exploration.
- Used SQLAlchemy create_engine to connect to the sqlite database.
- Used SQLAlchemy automap_base() to reflect the tables into classes and save a reference to those classes called Station and Measurement.
- Linked Python to the database by creating an SQLAlchemy session.

### Precipitation Analysis:
- Started by finding the most recent date in the data set and storing in python.
- Used this date, retrieved the last 12 months of precipitation data by querying the 12 preceding months of data.
- Selected only the date and prcp values.
- Loaded the query results into a Pandas DataFrame and set the index to the date column.
- Sorted the DataFrame values by date in descending order
- Plotted the results using the DataFrame plot method
- Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis
-- Designed a query to calculate the total number of stations in the dataset.
- Designed a query to find the most active stations (i.e. which stations have the most rows?).
- Listed the stations and observation counts in descending order.
- Identified the station id has the highest number of observations
- Used the most active station id to calculate the lowest, highest, and average temperature. 
- Designed a query to retrieve the last 12 months of temperature observation data (TOBS).
- Filtered by the station with the highest number of observations.
- Queried the last 12 months of temperature observation data for this station.
- Plotted the results as a histogram with bins=12.


## Step 2 - Climate App
- Flask API was designed based on the queries that were developed and mentioned above.
- Used Flask to create routes.

### Routes Established:

* /
- Home page.
- Lists all routes that are available.

* /api/v1.0/precipitation
- Converted the query results to a dictionary using date as the key and prcp as the value.
- Returned the JSON representation of your dictionary.

* /api/v1.0/stations
- Returned a JSON list of stations from the dataset.

* /api/v1.0/tobs
- Queried the dates and temperature observations of the most active station for the last year of data.
- Returned a JSON list of temperature observations (TOBS) for the previous year.

* /api/v1.0/<start> and /api/v1.0/<start>/<end>
- Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
- When only given the start date, calculated TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
- When given the start and the end date, calculated the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
