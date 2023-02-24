# sqlalchemy-challenge
Leverage SQL, SQLalchemy and Python to perform data exploration and climate analysis on a sqlite database. A climate app was created using Flask to contain the analysis on the web.

## Background

Data analysis was performed on a climate data for Honolulu, Hawaii for the period of 2010/01/01 - 2017/08/23. The database contains 2 tables, as follows:
- Statons: included ID, name, latitude, longitude and elevation for 9 weather stations
- Measurements: included observation date, temperature and precipitation


## Approach

- SQLalchemy was used to create an engine to connect to the sqlite database and run queries for data analytics

- Performed a query to retrieve the data and precipitation scores for the last 12 months and graph the data in a matplotlib bar chart.

<img width="400" alt="Screen Shot 2023-02-24 at 4 14 09 PM" src="https://user-images.githubusercontent.com/44728723/221295851-3de2d497-5565-4876-8bb7-f481ce2f7aa7.png">


- Performed queries to retrieve data and calculate the minimum, average and maximum temperature observations for the most active weather station.

- Performed a query to retrieve the last 12 months of temperature data and plot a histogram of the data

<img width="400" alt="Screen Shot 2023-02-24 at 4 14 25 PM" src="https://user-images.githubusercontent.com/44728723/221295770-ee3795bc-b12f-4b51-8471-14baec9be1c2.png">


- An app was created using flask which included a homepage with an image and 5 static routes as well as dynamic routes, including:
    - Precipitation: returns the last 12 months of precipitation observations with dates in JSON format
    - Stations: returns details of the 9 weather stations in JSON format
    - Temperatures (tobs):  returns the last 12 months of temperature observations with dates for the most active station in JSON format
    - Start: returns the MIN/AVG/MAX temperatures for a specified start date and end date in JSON format




## Technology
- sqlite database
- sqlalchemy
- matplotlib
- python
- pandas
- JSON
- flask

## Sources used for this analysis

Six (6) csv files including:
    - departments.csv
    - dept_emp.csv
    - dept_manager.csv
    - employees.csv
    - salaries.csv
    - titles.csv
