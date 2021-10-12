#!/usr/bin/env python3

"""

"""

import utils
import inputs


__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.7.2021"
__status__ = "Development"


def main():
    """

    :return: n/a
    """
    display_title()
    booking_day = inputs.day_of_week_input()
    price = calculate_price(booking_day)
    display_available_rooms(booking_day, 1, price)
    final_message()


def display_title():
    print("Python Programmer's Paradise - Motel Booking System")
    utils.display_line()


def calculate_price(booking_day):
    base_rate = 80
    if booking_day == 'SUNDAY':
        base_rate *= 1.2
    if booking_day == 'MONDAY':
        base_rate *= 1.2

    print('base rate:', round(base_rate))

    return base_rate


def display_available_rooms(booking_day, num_rooms, price):
    print(booking_day, 'AVAILABLE ROOMS')
    utils.display_line()
    print('num single  rooms (2 guest max) available at price')
    print('num double  rooms (4 guest max) available at price')
    print('num king    rooms (2 guest max) available at price')


def final_message():
    print('Your total bill is price.')
    print('We are looking forward to seeing you soon!')


# runs this specific module's main
if __name__ == "__main__":
    main()
