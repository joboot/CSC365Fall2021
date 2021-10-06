#!/usr/bin/env python3

"""
A menu for all of our farm calculators for Chapter 4's assignment
Combines all of the previous assignments that we have worked on into one menu
The user can choose which calculator to run from this menu and run them multiple times
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


def main():
    """
    Inputs:
    User input to keep running calculator menu
    User input to choose which calculator to run

    Outputs:
    Calculator menu
    Any calculator the user wants to run
    :return: n/a
    """
    display_title()
    menu()
    print("Program has ended.")


def display_title():
    """
    Displays title
    :return: n/a
    """
    print('Farm Calculators')
    validation.display_line()
    print()


def menu():
    """
    Menu in a while loop that runs all other calculators by user input
    :return: n/a
    """
    user_input = 'y'
    while user_input.lower() == 'y':
        print("1 - Cover Crop Calculator")
        print("2 - Break Even Calculator")
        print("3 - Stocking Rate Calculator")
        print("4 - Water Allocations Calculator")
        calc_input = validation.get_range('Which calculator would you like to run? ', 0, 4, 'int')
        print()
        if calc_input == 1:
            print("Running Cover Crop Calculator...")
            cover_crop_calculator.main()

        elif calc_input == 2:
            print("Running Break Even Calculator...")
            break_even_calc.main()

        elif calc_input == 3:
            print("Running Stocking Rate Calculator...")
            stocking_rate_calc.main()

        elif calc_input == 4:
            print("Running Water Allocations Calculator...")
            water_allocations_calc.main()

        print()
        print()
        user_input = input('Would you like to run another calculator?(y/n): ')
        print()


# runs this specific module's main
if __name__ == "__main__":
    main()
