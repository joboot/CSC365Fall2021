#!/usr/bin/env python3

"""
Utility code and validation code for output and data input from the user.
"""

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.7.2021"
__status__ = "Development"


def main():
    """

    :return: n/a
    """
    print('inputs main')
    day_of_week_input()


def day_of_week_input():
    while True:
        booking_day = input("Which day of the week will you be checking in?\nMonday - Sunday: ")
        booking_day = booking_day.lower()

        if booking_day == 'monday' or booking_day == 'm' or booking_day == 'mon':
            booking_day = 'MONDAY'
            return booking_day
        elif booking_day == 'tuesday' or booking_day == 't' or booking_day == 'tues':
            booking_day = 'TUESDAY'
            return booking_day
        elif booking_day == 'wednesday' or booking_day == 'w' or booking_day == 'wed':
            booking_day = 'WEDNESDAY'
            return booking_day
        elif booking_day == 'thursday' or booking_day == 'th' or booking_day == 'thurs':
            booking_day = 'THURSDAY'
            return booking_day
        elif booking_day == 'friday' or booking_day == 'f' or booking_day == 'fri':
            booking_day = 'FRIDAY'
            return booking_day
        elif booking_day == 'saturday' or booking_day == 'sa' or booking_day == 'sat':
            booking_day = 'SATURDAY'
            return booking_day
        elif booking_day == 'sunday' or booking_day == 'su' or booking_day == 'sun':
            booking_day = 'SUNDAY'
            return booking_day
        else:
            print("Please enter a day of the week correctly.")


# runs this specific module's main
if __name__ == "__main__":
    main()
