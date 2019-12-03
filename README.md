### Date created
03 December 2019

### Project Title
Explore US Bikeshare Data

### Description
This Python program explores U.S. bikeshare data. Statistics are used to analyse the data and provide answers about relevant questions. The program was validated against bikeshare data for New York, Washington and Chicago.

### Files used
Python program:                 
  bikeshare.py
Data Files (see .gitignore file):
  chicago.csv
  new_york_city.csv
  washington.csv

### Functions
get_filters()
  Asks user to specify a city, month, and day to analyze.
  Returns city, month, day

load_data(city, month, day)
  Loads data for the specified city and filters by month and day if applicable.
  Returns Pandas DataFrame containing city data filtered by month and day

view_raw_data(df, step, colwidth)
  Display portions of raw data.

time_stats(df)
  Displays statistics on the most frequent times of travel.

station_stats(df)
  Displays statistics on the most popular stations and trip.

trip_duration_stats(df)
  Displays statistics on the total and average trip duration.

user_stats(df)
  Displays statistics on bikeshare users.
  
additional_stats(df)
  Displays additional statistics.

### Credits
The basis for this project is Udacity's Programming for Data Science Degree.
The following websites were consulted in the execution of the projects:
1. http://www.datasciencemadesimple.com/
2. https://docs.python.org
3. https://data36.com/
4. https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
5. https://www.pythonprogramming.in/how-to-check-if-a-column-exists-in-pandas.html
