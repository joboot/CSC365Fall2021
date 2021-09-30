#!/usr/bin/env python3

"""
A stocking rate calculator for Chapter 3's assignment
Determines how many cow-calf pairs a pasture can support.
"""

import validation

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "9.30.2021"
__status__ = "Development"


def main():
    """
    Main function
    :return:
    """
    display_title()
    forage_per_acre = forage_samples()
    utilization_rate = utilization_rate_input()
    animal_unit_month = animal_unit_month_input()
    final_output(forage_per_acre, utilization_rate, animal_unit_month)
    print('Stocking Rate Calculator has ended.')


def display_title():
    """
    Displays title
    :return:
    """
    print('Cow-Calf Pair Pasture Stocking Rates')
    validation.display_line()


def forage_samples():
    """
    Gets user input on forage samples and calculates forage per acre
    :return forage_per_acre:
    """
    # only allows values 1-20
    forage_samples_taken = validation.get_int('Enter the number of forage samples taken (1-20): ', 0, 20)

    print()
    print("Please enter dry clipping samples in grams:")

    clipping_sample_weight = 0

    # for loop to get user input on sample weights in grams
    # adds up to total weight of samples
    for i in range(forage_samples_taken):
        clipping_sample_weight = clipping_sample_weight + int(input("Sample #" + str(i+1) + ": "))

    print()

    # calculating square foot average per pound and rounding it to the third decimal
    square_foot_avg_lbs = round((clipping_sample_weight / forage_samples_taken) / 453.592, 3)

    # calculating forage per acre and rounding it
    forage_per_acre = round(square_foot_avg_lbs * 43560)

    print('Square foot average per lb =', square_foot_avg_lbs)
    print('Forage per acre in lbs =', forage_per_acre)
    print()
    return forage_per_acre


def utilization_rate_input():
    """
    Gets user input on utilization rate
    :return utilization_rate:
    """
    # only allows values 1-100
    utilization_rate = validation.get_int('Enter the utilization rate (1-100): ', 0, 100)

    print()
    return utilization_rate


def animal_unit_month_input():
    """
    Gets user input on animal unit month
    :return animal_unit_month:
    """
    # only allows values 1-2000
    animal_unit_month = validation.get_int('Enter the AUM (animal unit month) in lbs (1-2000): ', 0, 2000)

    return animal_unit_month


def final_output(forage_per_acre, utilization_rate, animal_unit_month):
    """
    Calculates stocking rate and prints final output
    :param forage_per_acre:
    :param utilization_rate:
    :param animal_unit_month:
    :return:
    """
    # calculating and rounding final stocking rate
    stocking_rate = round((forage_per_acre * (utilization_rate/100)) / animal_unit_month, 2)

    print()
    print("Stocking rate (cow-calf per acre) =", stocking_rate)
    print()


# runs this specific module's main
if __name__ == "__main__":
    main()
