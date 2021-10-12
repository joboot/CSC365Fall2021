#!/usr/bin/env python3

"""
Code for all of user input pertaining to main module
"""

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.7.2021"
__status__ = "Development"

import utils


def main():
    """
    Testing input functions
    :return: n/a
    """
    print('inputs main')
    room_type = 'SINGLE'
    num_guests = 2
    price = 50
    day_of_week_input()
    room_input()
    guest_input(room_type)
    night_input(room_type, num_guests, price)


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


def room_input():
    print()
    while True:
        room_type = input("What type of room would you like to stay in?\ns = single, d = double, k = king: ")
        room_type = room_type.lower()
        if room_type == 'single' or room_type == 's':
            room_type = 'SINGLE'
            return room_type
        elif room_type == 'double' or room_type == 'd':
            room_type = 'DOUBLE'
            return room_type
        elif room_type == 'king' or room_type == 'k':
            room_type = 'KING'
            return room_type
        else:
            print("Please enter the room type correctly.")


def guest_input(room_type):
    print()
    while True:
        if room_type == 'SINGLE':
            num_guests = utils.get_range("How many guests will be staying in the " + room_type +
                                         " room: ", 0, 2, 'int')
            return num_guests
        elif room_type == 'DOUBLE':
            num_guests = utils.get_range("How many guests will be staying in the " + room_type +
                                         " room: ", 0, 4, 'int')
            return num_guests
        elif room_type == 'KING':
            num_guests = utils.get_range("How many guests will be staying in the " + room_type +
                                         " room: ", 0, 2, 'int')
            return num_guests
        print()


def night_input(room_type, num_guests, price):
    print()
    num_nights = utils.get_positive_num(
        'How many days do you want to book a ' + room_type + ' room, with ' + str(num_guests) +
        ' guests, at ' + str(price) + ' a night: ')
    print()

    return num_nights


# runs this specific module's main
if __name__ == "__main__":
    main()
