import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

PERMISSIBLE_MONTHS = ('all', 'january', 'february', 'march', 'april', 'may', 'june')

PERMISSIBLE_DAYS = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Please enter the filter criteria:')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print('\n>>>')
        city = input('Please enter the name of the city to analyze (Chicago, New York City or Washington).\n\t')
        if city.lower() in CITY_DATA.keys():
            print("\tBikeshare analysis will be performed for CITY: ", city.title())
            print('\t<<<\n')
            break
        else:
            print("\t!!! Invalid city name, please select option from {}\n".format(CITY_DATA.keys()))

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print('\n>>>')
        month = input('Please enter the name of the month to analyze (All, January, February, ... , June).\n\t')
        if month.lower() in PERMISSIBLE_MONTHS:
            print("\tBikeshare analysis will be performed for MONTH: ", month.title())
            print('\t<<<\n')
            break
        else:
            print("\t!!! Invalid month, please select an option from {}\n".format(PERMISSIBLE_MONTHS))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('\n>>>')
        day = input('Please enter the name of the day to analyze (All, Monday, Tuesday, ... , Sunday).\n\t')
        if day.lower() in PERMISSIBLE_DAYS:
            print("\tBikeshare analysis will be performed for DAY: ", day.title())
            print('\t<<<\n')
            break
        else:
            print("\t!!! Invalid day, please select an option from {}\n".format(PERMISSIBLE_DAYS))

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Get filename
    filename = CITY_DATA[city.lower()]
    print('\n>>>')
    print('Reading csv data from: ', filename)
    df = pd.read_csv(filename);
    print('\tRetrieved {} unformatted rows and with {} columns'.format(df.shape[0], df.shape[1]))
    print('\t<<<\n')

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Create new columns for filtering by month and day
    df['month'] =  df['Start Time'].dt.month
    df['day_of_week'] =  df['Start Time'].dt.weekday_name

    #Filter by month (if necessary - no need to add 1, 'All' in zeroth position is sufficient)
    index = PERMISSIBLE_MONTHS.index(month.lower())
    if month.lower() != 'all':
        print('\n>>>')
        print('\tFiltering by month: {}, index: {}'.format(month, index))
        df = df[df['month'] == index]
        print('\t<<<\n')

    #Filter by day (if necessary)
    if day.lower() != 'all':
        print('\n>>>')
        print('\tFiltering by day: ', day)
        df = df[df['day_of_week'] == day.title()]
        print('\t<<<\n')

    #Create extra columns for subsequent analysis
    df['hour'] = df['Start Time'].dt.hour
    df['Route'] = df['Start Station'] + ' to ' + df['End Station']

    print('-'*40)
    return df

def view_raw_data(df, step, colwidth):
    #Variables
    #   df:         Dataframe to inspect
    #   step:       Number of rows to show
    #   colwidth    Desired column width (attempt to show all columns)

    pd.set_option('max_colwidth', colwidth)
    for i in range(0, df.shape[0], step):
        print("\nRaw data in rows: {} to {}".format(i, i+step-1))
        print('-'*40)
        print(df[i:i+step])
        show_more_data = input('Would you like to see more data? (yes/ no)\n\t')
        if show_more_data.lower() != "yes":
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    frequent_month = PERMISSIBLE_MONTHS[df['month'].mode()[0]]
    print("The most common month is: ", frequent_month.title())

    # TO DO: display the most common day of week
    frequent_day = df['day_of_week'].mode()[0]
    print("The most common day is: ", frequent_day)

    # TO DO: display the most common start hour
    frequent_hour = df['hour'].mode()[0]
    print("The most common hour is: ", frequent_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    frequent_start_station = df['Start Station'].mode()[0]
    print("\tThe most commonly used start station is: ", frequent_start_station)

    # TO DO: display most commonly used end station
    frequent_end_station = df['End Station'].mode()[0]
    print("\tThe most commonly used end station is: ", frequent_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_route = df['Route'].mode()[0]
    print("\tThe most commonly used route is: ", frequent_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\tThe total trip duration is: {} seconds".format(df["Trip Duration"].sum()))

    # TO DO: display mean travel time
    print("\tThe mean trip duration is: {} seconds".format(df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nUser Type Counts: \n", df['User Type'].value_counts())

    # TO DO: Display counts of gender
    #Exception handling method 1: Check if name in columns
    if "Gender" in df.columns:
        print("\nGender Counts: \n", df['Gender'].value_counts())
    else:
        print("\n\t The column [Gender] does not exist, no value counts related to this can be presented.")

    # TO DO: Display earliest, most recent, and most common year of birth
    #Exception handling method 2: Try/Catch
    try:
        print("\n\tThe earliest birth year is: ", int(df['Birth Year'].min()), " seconds")
        print("\tThe most recent birth year is: ", int(df['Birth Year'].max()), " seconds")
        print("\tThe most common bith year is: ",int(df['Birth Year'].mode()[0]), " seconds")
    except:
        print("\n\t The column [Birth Year] does not exist, no information concerning this can be presented.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def additional_stats(df):
    """Displays additional statistics."""

    print('\nDisplay Additional Statistics...\n')
    start_time = time.time()

    print("Number of trips per: ",df.groupby('User Type')["Route"].count(),"\n")
    print("Mean trip duration per: ",df.groupby('User Type')['Trip Duration'].mean(),"\n")

    print("The number of routes with the same start and end station: ", df[df['Start Station'] == df['End Station']]["Route"].count())
    popular_route = df[df['Start Station'] == df['End Station']]["Route"].mode()[0];
    print("The most popular trip of this type is: ", popular_route)
    print("\tThe maximum trip duration is", df[df["Route"] == popular_route]["Trip Duration"].max())
    print("\tThe mean trip duration is", df[df["Route"] == popular_route]["Trip Duration"].mean())
    print("\tThe minimum trip duration is", df[df["Route"] == popular_route]["Trip Duration"].min())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    """
    Accept user interaction in loop.

    Exit loop when user provides answer other than "yes"
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        view_raw_data(df, 10,10)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        additional_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
