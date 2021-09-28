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

LINE_LENGTH = 60


# main function
def main():
    """
    ain function
    What is supposed to run for the program
    :return: none
    """
    display_title()


def display_title():
    """
    Displays title and initial question
    :return: none
    """
    print(f'{"Farm Calculators":>37}')
    print('=' * LINE_LENGTH)
    print()
    print('Which calculator would you like to run?')


# runs this specific module's main
if __name__ == "__main__":
    main()
