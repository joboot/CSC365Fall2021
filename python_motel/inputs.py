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
    booking_day = input("Which day of the week will you be checking in?\nMonday - Sunday: ")
    booking_day = booking_day.lower()
    print(booking_day)
    print(booking_day.lower())
    while True:
        if booking_day == "monday" or 'm':
            booking_day = 'MONDAY'
            print('booking day:', booking_day)
            return booking_day
        elif booking_day == "tuesday" or 't':
            booking_day = 'TUESDAY'
            print('booking day:', booking_day)
            return booking_day
        elif booking_day.lower() == "wednesday" or 'w':
            booking_day = 'WEDNESDAY'
            print('booking day:', booking_day)
            return booking_day
        elif booking_day.lower() == "thursday" or 'th':
            booking_day = 'THURSDAY'
            print('booking day:', booking_day)
            return booking_day
        elif booking_day.lower() == "friday" or 'f':
            booking_day = 'FRIDAY'
            print('booking day:', booking_day)
            return booking_day
        elif booking_day.lower() == "saturday" or 'sa':
            booking_day = 'SATURDAY'
            print('booking day:', booking_day)
            return booking_day
        elif booking_day.lower() == "sunday" or 'su':
            booking_day = 'SUNDAY'
            print('booking day:', booking_day)
            return booking_day
        else:
            "Please enter a day of the week correctly."
        print(booking_day)


# runs this specific module's main
if __name__ == "__main__":
    main()
