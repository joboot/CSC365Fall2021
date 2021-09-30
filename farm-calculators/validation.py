#!/usr/bin/env python3

"""
Validation code for data input from the user.
Keeps the user from entering floats or integers outside of range specified
"""

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "9.30.2021"
__status__ = "Development"

LINE_LENGTH = 60


def main():
    """
    Test code
    :return:
    """
    display_line()
    get_float("Float input 1-10: ", 1.0, 10.0)
    get_int('Int input 1-10: ', 1, 10)


def display_line():
    """
    Displays a line for program output
    :return:
    """
    print('=' * LINE_LENGTH)


def get_float(prompt, low, high):
    """
    Validator to keep input floats inside of a range
    :param prompt: Message to prompt user for input
    :param low: low number for input
    :param high: high number for input
    :return: none
    """
    while True:
        number = float(input(prompt))
        if low <= number <= high:
            return number
        else:
            print("Entry must be greater than or equal to", low,
                  "and less than or equal to", high)


def get_int(prompt, low, high):
    """
    Validator to keep input integers inside of a range
    :param prompt: Message when the user uses wrong input
    :param low: low number for input
    :param high: high number for input
    :return: none
    """
    while True:
        number = int(input(prompt))
        if low < number <= high:
            return number
        else:
            print("Entry must be greater than or equal to", low,
                  "and less than or equal to", high)


# runs this specific module's main
if __name__ == "__main__":
    main()
