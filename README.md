# sqlalchemy-challenge
Leverage SQLalchemy, Python and Flask to perform data exploration and data analysis on a sqlite database. A climate app API was created using Flask to contain the analysis.

## Background

Data analysis was performed on a climate data for Honolulu, Hawaii for the period of 2010/01/01 - 2017/08/23. The database contains 2 tables, as follows:
- Statons: included ID, name, latitude, longitude and elevation for 9 weather stations
- Measurements: included observation date, temperature and precipitation


## Approach

- SQLalchemy was used to create an engine to connect to the sqlite database and run queries for data analytics

- Performed a query to retrieve the data and precipitation scores for the last 12 months and graph the data in a matplotlib bar chart.

<p align="center">
  <img width="400" alt="Screen Shot 2023-02-24 at 4 14 09 PM" src="https://user-images.githubusercontent.com/44728723/221295851-3de2d497-5565-4876-8bb7-f481ce2f7aa7.png">
</p>

- Performed queries to retrieve data and calculate the minimum, average and maximum temperature observations for the most active weather station.

- Performed a query to retrieve the last 12 months of temperature data and plot a histogram of the data

<p align="center">
    <img width="400" alt="Screen Shot 2023-02-24 at 4 14 25 PM" src="https://user-images.githubusercontent.com/44728723/221295770-ee3795bc-b12f-4b51-8471-14baec9be1c2.png">
</p>

- An API app was created using flask which included a homepage with an image and 5 static routes as well as dynamic routes, including:
    - Precipitation: returns the last 12 months of precipitation observations with dates in JSON format
    - Stations: returns details of the 9 weather stations in JSON format
    - Temperatures (tobs):  returns the last 12 months of temperature observations with dates for the most active station in JSON format
    - Start: returns the MIN/AVG/MAX temperatures for a specified start date and end date in JSON format

<p align="center">
  <img width="364" alt="climate api website" src="https://user-images.githubusercontent.com/44728723/221297504-2a89ed39-6bbb-459b-bb8b-656de1c90ff2.png">
</p>


## Technology
- sqlite database
- sqlalchemy
- matplotlib
- python
- pandas
- JSON
- flask

## Sources used for this analysis
- hawaii.sqlite
