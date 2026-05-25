#Write a function called check_date. check_date should
#require two positional parameters: a string representing
#the name of a month, and an integer representing a date.
#check_date should also have a keyword parameter called
#is_leap_year, assumed to be False, representing whether or
#not it's a leap year.
#
#Return True if the date is a valid calendar date. Return
#False if it is not. A date may not be a valid calendar
#date if the month isn't a real month, or if that date does
#not exist for that month. You can see some examples at the
#end of this file.
#
#Remember: 30 days has September, April, June, and November.
#All the rest have 31, except February, which has 28, until
#Leap Year gives it 29.
#
#You may assume that day will be greater than 0 (you don't
#need to check negative or zero values for day).


#Write your function here!
def check_date(month, date, is_leap_year = False):
    real_date = {
        "January" : 31,
        "February" : 28,
        "March" : 31,
        "April" : 30,
        "May" : 31,
        "June" : 30,
        "July" : 31,
        "August" : 31,
        "September" : 30,
        "October" : 31,
        "November" : 30,
        "December" : 31,
    }

    if is_leap_year:
        real_date["February"] = 29

    return month in real_date and date <= real_date[month]




