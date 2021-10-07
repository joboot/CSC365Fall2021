#!/usr/bin/env python3

"""

"""

import utils


__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.7.2021"
__status__ = "Development"


def main():
    """

    :return: n/a
    """
    display_title()
    display_available_rooms()
    final_message()


def display_title():
    print("Python Programmer's Paradise - Motel Booking System")
    utils.display_line()


def display_available_rooms():
    print('day AVAILABLE ROOMS')
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