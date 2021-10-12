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

    while True:

        booking_day = inputs.day_of_week_input()

        single_room_price, double_room_price, king_room_price = calculate_room_price(booking_day)

        display_available_rooms(booking_day, 1, single_room_price, double_room_price, king_room_price)

        room_type = inputs.room_input()

        num_guests = inputs.guest_input(room_type)

        surcharge = calculate_surcharge(num_guests)

        price = calculate_price(room_type, single_room_price, double_room_price, king_room_price, surcharge)

        num_nights = inputs.night_input(room_type, num_guests, price)

        total_price = calculate_total_price(num_nights, price)

        while True:
            user_confirm = utils.get_yn(
                "Please confirm the booking for " + str(num_nights) + " nights total = " + str(total_price) +
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
    print("Python Programmer's Paradise - Motel Booking System")
    utils.display_line()


def calculate_total_price(num_nights, price):
    total_price = num_nights * price

    return total_price


def calculate_room_price(booking_day):
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

    :param guest_amount: This is the amount of guests staying in the room
    :return:
    """
    if guest_amount == 1:
        surcharge = 0
    elif guest_amount == 2:
        surcharge = 10
    elif guest_amount == 3:
        surcharge = 18
    elif guest_amount == 4:
        surcharge = 32

    print('There is a ' + str(surcharge) + ' surcharge based for ' + str(guest_amount) + ' guests.')
    int(surcharge)

    return surcharge


def display_available_rooms(booking_day, num_rooms, single_room_price, double_room_price, king_room_price):
    print()
    print(booking_day, 'AVAILABLE ROOMS')
    utils.display_line()
    print(num_rooms, 'single rooms (2 guest max) available at', single_room_price)
    print(num_rooms, 'double rooms (4 guest max) available at', double_room_price)
    print(num_rooms, 'king   rooms (2 guest max) available at', king_room_price)


def final_message(total_price):
    print()
    print(f'{"Your total bill is", total_price}')
    print('We are looking forward to seeing you soon!')


# runs this specific module's main
if __name__ == "__main__":
    main()
