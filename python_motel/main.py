#!/usr/bin/env python3

"""
Main module for the Mid-term assignment
This a booking system for Python Programmers Paradise Motel
Calculates prices based on the day of the week and allows user to book the motel rooms for those days
"""

import utils
import inputs


__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.7.2021"
__status__ = "Development"


def main():
    """
    Inputs:
    Booking day (Monday - Sunday)
    Room type chosen (Single, Double, and King)
    Number of guests
        single (2 person max)
        double (4 person max)
        king (2 person max)
    Number of nights staying
    User input to confirm bill
    User input if wanting to book another room

    Outputs:
    Title
    User prompt to choose which day to book
    Room types and prices
        DOW = day of week
        Base rate of $80
        Single is DOW rate
        Double is DOW rate + 50% increase
        King is DOW rate + 25% increase
    Random number of available rooms
        0 to 8 singles rooms
        0 to 10 doubles rooms
        0 to 2 kings rooms
    User prompt to choose which room to stay in
    User prompt to enter how many guests are staying
    Surcharge
        1 person = no surcharge
        2 people = $10 surcharge
        3 people = $18 surcharge
        4 people = $32 surcharge
    User prompt to enter how many nights staying
    Price of room
        Base rate of $80
        Sunday, Monday, and Tuesday are base rate + 20%
        Wednesday and Thursday are base rate + 10%
        Friday and Saturday are just base rate
    User prompt to confirm booking
    User prompt to ask if user wants to book another room
    Total bill
        Number of nights * price of room
    Final message

    :return: n/a
    """
    display_title()

    rand_single_room = utils.create_rand_num(9)
    rand_double_room = utils.create_rand_num(11)
    rand_king_room = utils.create_rand_num(3)

    while True:

        booking_day = inputs.day_of_week_input()

        single_room_price, double_room_price, king_room_price = calculate_room_price(booking_day)

        display_available_rooms(booking_day, rand_single_room, rand_double_room, rand_king_room, single_room_price,
                                double_room_price, king_room_price)

        room_type, rand_single_room, rand_double_room, rand_king_room = \
            inputs.room_input(rand_single_room, rand_double_room, rand_king_room)

        num_guests = inputs.guest_input(room_type)

        surcharge = calculate_surcharge(num_guests)

        price = calculate_price(room_type, single_room_price, double_room_price, king_room_price, surcharge)

        num_nights = inputs.night_input(room_type, num_guests, price)

        total_price = calculate_total_price(num_nights, price)

        while True:
            user_confirm = utils.get_yn(
                "Please confirm the booking for " + str(num_nights) + " nights total = $" + str(total_price) +
                "\ny = Yes, n = No: ")
            if user_confirm == 'y':
                break
            else:
                print('Booking cancelled.')
                total_price = 0
                break

        print()
        user_loop = utils.get_yn('Do you want to book another room?\ny = Yes, n = No: ')
        if user_loop == 'n':
            final_message(total_price)
            break


def display_title():
    """
    Displays title
    :return: n/a
    """
    print("Python Programmer's Paradise - Motel Booking System")
    utils.display_line()


def calculate_total_price(num_nights, price):
    """
    Calculates the total price of the stay (Number of nights * price of room)
    :param num_nights: Number of nights staying
    :param price: Total price of the room per night
    :return: Total price of the stay
    """
    total_price = num_nights * price

    return total_price


def calculate_room_price(booking_day):
    """
    Calculates the room price based on the day of the week
    :param booking_day: Day the user is booking
    :return: Prices of the rooms that day
    """
    base_rate = 80
    if booking_day == 'SUNDAY':
        base_rate *= 1.2
    elif booking_day == 'MONDAY':
        base_rate *= 1.2
    elif booking_day == 'TUESDAY':
        base_rate *= 1.2
    elif booking_day == 'WEDNESDAY':
        base_rate *= 1.1
    elif booking_day == 'THURSDAY':
        base_rate *= 1.1

    single_room_price = round(base_rate)
    double_room_price = round(base_rate * 1.5)
    king_room_price = round(base_rate * 1.25)

    return single_room_price, double_room_price, king_room_price


def calculate_price(room_type, single_room_price, double_room_price, king_room_price, surcharge):
    """
    Calculate the price of the room based on room type and adds surcharge to it per
    :param room_type: Type of room (single, double, king)
    :param single_room_price: Price of a single room
    :param double_room_price: Price of a double room
    :param king_room_price: Price of a king room
    :param surcharge: surcharge based off the amount of guests
    :return: Price of the staying 1 night in the room
    """
    room_price = 0
    if room_type == 'SINGLE':
        room_price = single_room_price
    elif room_type == 'DOUBLE':
        room_price = double_room_price
    elif room_type == 'KING':
        room_price = king_room_price

    price = room_price + surcharge

    return price


def calculate_surcharge(guest_amount):
    """
    Calculates the surcharge based on the amount of guests staying in the room
    :param guest_amount: This is the amount of guests staying in the room
    :return: The surcharge based on the amount of guests
    """
    surcharge = 0
    if guest_amount == 1:
        surcharge = 0
    elif guest_amount == 2:
        surcharge = 10
    elif guest_amount == 3:
        surcharge = 18
    elif guest_amount == 4:
        surcharge = 32

    print('There is a $' + str(surcharge) + ' surcharge based for ' + str(guest_amount) + ' guests.')
    int(surcharge)

    return surcharge


def display_available_rooms(booking_day, rand_single_room, rand_double_room, rand_king_room, single_room_price,
                            double_room_price, king_room_price):
    """
    Displays a table of available rooms and their prices for the booking day chosen
    :param booking_day: Booking day the user has chosen
    :param rand_single_room: Random number of available single rooms
    :param rand_double_room: Random number of available double rooms
    :param rand_king_room: Random number of available king rooms
    :param single_room_price: Price of a single room
    :param double_room_price: Price of a double room
    :param king_room_price: Price of a king room
    :return: n/a
    """
    print()
    print(booking_day, 'AVAILABLE ROOMS')
    utils.display_line()
    print(rand_single_room, 'single rooms (2 guest max) available at $' + str(single_room_price))
    print(rand_double_room, 'double rooms (4 guest max) available at $' + str(double_room_price))
    print(rand_king_room, 'king   rooms (2 guest max) available at $' + str(king_room_price))


def final_message(total_price):
    """
    Final message outputting the total bill
    :param total_price: Total bill for the stay
    :return: n/a
    """
    print()
    print("Your total bill is $" + str(total_price))
    print('We are looking forward to seeing you soon!')


# runs this specific module's main
if __name__ == "__main__":
    main()
