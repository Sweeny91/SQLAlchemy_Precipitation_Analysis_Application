# SQLAlchemy driven Application for Preicipitation Analysis

- In this section of the course we were introduced to the powerful library know as SQLAlchemy. This library lets users interact with databases condensed into files such as sqlite using SQL syntax. This has been found very valuable and can be used together with libraries such as datetime, pandas, and matplotlib to visualize data in an informative manner. 
- The concepts of clients and servers were revisited and with these concepts students we introduced to the Flask library and were allowed to establish API endpoints that can be accessed on the front-end. The ability of users to publicize their findinds via APIs is a way of operating on a very high level of the internet and be very beneficial to the client.

## Given Background

- A theoretical sitiation was given where students we asked to use the skills mentions above using real world data in order to showcase out understand of SQLAlchemy and Flask libraries.
- This theoretical background is given below for readers to better understand the data provided in this repository.

![surfs-up.png](Images/surfs-up.png)

""" Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.

## Step 1 - Climate Analysis and Exploration

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Use the provided [hawaii.sqlite](Resources/hawaii.sqlite) file to complete your climate analysis and data exploration.

## Step 2 - Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use Flask to create your routes.


## BONUS: (COMPLETED)

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.
* Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

### Temperature Analysis II

* You are looking to take a trip from August first to August seventh of this year, but are worried that the weather will be less than ideal. Using historical data in the dataset find out what the temperature has previously looked like.
* Plot the min, avg, and max temperature from your previous query as a bar chart.
  * Use "Trip Avg Temp" as the title.
  * Use the average temperature as the bar height (y value).
  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

    ![temperature](Images/temperature.png)

### Daily Rainfall Average

* Calculate the rainfall per weather station using the previous year's matching dates.
  * Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.
 
  ![daily-normals](Images/daily-normals.png)
  
 """

# Deliverables:

## Precipitation Analysis

* Started by finding the most recent date in the data set and storing in python.
* Used this date, retrieved the last 12 months of precipitation data by querying the 12 preceding months of data.
* Selected only the date and prcp values.
* Loaded the query results into a Pandas DataFrame and set the index to the date column.
* Sorted the DataFrame values by date in descending order
* Plotted the results using the DataFrame plot method
* Used Pandas to print the summary statistics for the precipitation data.

  ![precipitation](Images/precipitation.png)


## Station Analysis

* Designed a query to calculate the total number of stations in the dataset.
* Designed a query to find the most active stations (i.e. which stations have the most rows?).
* Listed the stations and observation counts in descending order.
* Identified the station id has the highest number of observations
* Used the most active station id to calculate the lowest, highest, and average temperature. 
* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).
* Filtered by the station with the highest number of observations.
* Queried the last 12 months of temperature observation data for this station.
* Plotted the results as a histogram with bins=12.

    ![station-histogram](Images/station-histogram.png)

## Routes Established:

### /
- Home page.
- Lists all routes that are available.

### /api/v1.0/precipitation
- Converted the query results to a dictionary using date as the key and prcp as the value.
- Returned the JSON representation of your dictionary.

### /api/v1.0/stations
- Returned a JSON list of stations from the dataset.

### /api/v1.0/tobs
- Queried the dates and temperature observations of the most active station for the last year of data.
- Returned a JSON list of temperature observations (TOBS) for the previous year.

### /api/v1.0/start & /api/v1.0/start/end
- Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
- When only given the start date, calculated TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
- When given the start and the end date, calculated the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
- - -
