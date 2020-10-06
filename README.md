In this project I used SQLAlchemy create_engine to connect to my sqlite database.

Used SQLAlchemy automap_base() to reflect my tables into classes and save a reference to those classes called Station and Measurement.

## Precipitation Analysis


Designed a query to retrieve the last 12 months of precipitation data.


Selected only the date and prcp values.


Loaded the query results into a Pandas DataFrame and set the index to the date column.


Sorted the DataFrame values by date.


Plotted the results using the DataFrame plot method.

Used Pandas to print the summary statistics for the precipitation data.



## Station Analysis


Designed a query to calculate the total number of stations.


Designed a query to find the most active stations.


Listed the stations and observation counts in descending order.


Identified which station has the highest number of observations?




Designed a query to retrieve the last 12 months of temperature observation data (TOBS).


Filtered by the station with the highest number of observations.


Plotted the results as a histogram with bins=12.

