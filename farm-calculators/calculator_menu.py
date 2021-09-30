#!/usr/bin/env python3

"""
A menu for all of our farm calculators for Chapter 4's assignment
Combines all of the previous assignments that we have worked on into one menu
"""

import validation
import cover_crop_calculator
import break_even_calc
import stocking_rate_calc
import water_allocations_calc

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "9.28.2021"
__status__ = "Development"


# main function
def main():
    """
    main function
    What is supposed to run for the program
    :return: none
    """
    display_title()
    menu()
    print("Program has ended.")


def display_title():
    """
    Displays title and initial question
    :return: none
    """
    print('Farm Calculators')
    validation.display_line()
    print()


def menu():
    user_input = 'y'
    while user_input.lower() == 'y':
        print("1 - Cover Crop Calculator")
        print("2 - Break Even Calculator")
        print("3 - Stocking Rate Calculator")
        print("4 - Water Allocations Calculator")
        calc_input = int(input('Which calculator would you like to run? '))

        if calc_input == 1:
            print()
            print("Running Cover Crop Calculator...")
            print()
            cover_crop_calculator.main()

        if calc_input == 2:
            print()
            print("Running Break Even Calculator...")
            print()
            break_even_calc.main()

        if calc_input == 3:
            print()
            print("Running Stocking Rate Calculator...")
            print()
            stocking_rate_calc.main()

        if calc_input == 4:
            print()
            print("Running Water Allocations Calculator...")
            print()
            water_allocations_calc.main()

        print()
        user_input = input('Would you like to run another calculator?(y/n): ')
        print()


# runs this specific module's main
if __name__ == "__main__":
    main()
