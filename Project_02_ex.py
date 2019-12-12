
import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': '../../../CSV files/chicago.csv',
              'new york city':  '../../../CSV files/new_york_city.csv',
              'washington':  '../../../CSV files/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze All.
    """



    """
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """



    print('Hello! Let\'s explore some US bikeshare data!')


    city = input('enter city name: ')
    cities = ["chicago" , "new york city" , "washington"]
    while city.lower().strip() not in cities  :

         city = input("You entered unvalid  city, please re-enter city name : ")


    months = ['January','Feburary','March','April','May','June','July','Augest','Septemper','Octobr','November','December','All']
    month = input("which month you want to be filltered by? or type all for whole year?  ")
    while  month.title().strip()  not in months :
        month =input ("please enter a valid month number or type all: ")





    day = input("Enter a day or type all: ")

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thrusday", "Friday","Saturday" , "All"]
    while day.title().strip() not in days :
        day = input("please enter a valid day: ")





    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    city = city.lower().strip()
    month = month.title().strip()
    day = day.title().strip()
    print('-'*40)
    return city  , month , day


def load_data(city, month, day):
    """
    Loads data for the  city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city] )

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['day'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month_name()

    # filter by month if applicable
    if month != 'All':
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("common month is: \n ",common_month)

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print("common month is: \n ",common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour:\n{} \n".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_s_station = df['Start Station'].mode()[0]

    print("Most common start satation : \n",popular_s_station)

    # TO DO: display most commonly used end station
    popular_e_station = df['End Station'].mode()[0]
    print("Most common end satation :  \n",popular_e_station)
    # TO DO: display most frequent combination of start station and end station trip

    frequent_combination =  pd.DataFrame(df.loc[:,'Start Station']+ " TO : " + df.loc[:,'End Station']).mode()

    print("most frequent combination of start station and end station trip : \n",frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("total travel time is : \n",total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("average travel time is : \n",int(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    df1 = df[df['User Type']=="Subscriber"]
    Subscribers = df1['User Type'].count()
    print("Subscribers count is: \n", Subscribers)

    df2 = df[df['User Type']=="Customer"]
    Customers = df2['User Type'].count()
    print("Customers count is: \n", Customers)


    # TO DO: Display counts of gender
    df3 = df[df['Gender']=="Female"]
    females = df3['Gender'].count()
    print("Female count is: \n", females)

    df4 = df[df['Gender']=="Male"]
    Males = df4['Gender'].count()
    print("Male count is: \n", Males)

    # TO DO: Display earliest, most recent, and most common year of birth
    oldest = df['Birth Year'].min()
    print("The oldest client was born in: \n", int(oldest))

    youngest = df['Birth Year'].max()
    print("The youngest client was born in: \n", int(youngest))

    common_year =  df['Birth Year'].mode()
    print("The most common year of birth is: \n", int(common_year))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
