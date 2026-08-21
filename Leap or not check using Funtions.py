# Number of days in each month.
# The first value is 0 because month numbers start from 1.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Function to check whether a year is a leap year
def is_leap(year):

    # A leap year is divisible by 4
    # But years divisible by 100 are not leap years
    # unless they are also divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Function to find the number of days in a particular month
def days_in_month(year, month):

    # Check whether the month is between 1 and 12
    if not 1 <= month <= 12:
        return 'Invalid month'

    # February has 29 days in a leap year
    if month == 2 and is_leap(year):
        return 29

    # Return the number of days from the month_days list
    return month_days[month]


# Check whether 2017 is a leap year
print(is_leap(2017))
