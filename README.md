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
__get_filters()__
  * Asks user to specify a city, month, and day to analyze.
  * Returns city, month, day

__load_data(city, month, day)__
  * Loads data for the specified city and filters by month and day if applicable.
  * Returns Pandas DataFrame containing city data filtered by month and day

__view_raw_data(df, step, colwidth)__
  * Display portions of raw data.

__time_stats(df)__
  * Displays statistics on the most frequent times of travel.

__station_stats(df)__
  * Displays statistics on the most popular stations and trip.

__trip_duration_stats(df)__
  * Displays statistics on the total and average trip duration.

__user_stats(df)__
  * Displays statistics on bikeshare users.

__additional_stats(df)__
  * Displays additional statistics.

### Credits
The basis for this project is Udacity's Programming for Data Science Degree.
The following websites were consulted in the execution of the projects:
1. http://www.datasciencemadesimple.com/
2. https://docs.python.org
3. https://data36.com/
4. https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
5. https://www.pythonprogramming.in/how-to-check-if-a-column-exists-in-pandas.html
