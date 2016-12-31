#! /usr/bin/env python

# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


def get_days_in_month(month, year):
    days_in_month = {
        0: 31,
        2: 31,
        3: 30,
        4: 31,
        5: 30,
        6: 31,
        7: 31,
        8: 30,
        9: 30,
        10: 31,
        11: 31
    }

    if month in days_in_month:
        days = days_in_month[month]

    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days = 29

    else:
        days = 28

    return days


def count_sundays(start, end):

    # count up until the start date
    current_day = 1
    for year in range(1900, start):
        for month in range(12):
            current_day = (current_day + get_days_in_month(month, year)) % 7

    sundays = 0
    for year in range(1900, end):
        for month in range(12):

            if current_day == 0:
                sundays += 1

            current_day = (current_day + get_days_in_month(month, year)) % 7

    return sundays


print count_sundays(1901, 2000)
