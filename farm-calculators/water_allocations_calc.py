#!/usr/bin/env python3

"""
A irrigation water allocations calculator for paired programming assignment 2
This program calculates and determines how long it will take to use up an allocation of water for irrigation.
"""

import validation

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "9.30.2021"
__status__ = "Development"


def main():
    """
    Main function surrounded in a while loop based on user input
    :return:
    """
    user_input = 'y'
    # While loop intakes user input on whether or not they would like to calculate
    while user_input.lower() == 'y':

        display_title()
        irrigation_water_allocation, irrigated_area, average_flow_rate = user_inputs()
        rained_allocation_depth = calculations(irrigation_water_allocation, irrigated_area, average_flow_rate)
        final_output(irrigation_water_allocation, irrigated_area, average_flow_rate, rained_allocation_depth)

        # ask user if they would like to make another calculation, if not, break out of main while loop
        print()
        user_input = input('Would you like to make another calculation?(y/n): ')
        print()
    print('Water Allocations Calculator has ended.')


def display_title():
    """
    Displays title
    :return:
    """
    # Program header
    print('Irrigation Water Allocations Calculator')
    validation.display_line()


def user_inputs():
    """
    Gets user inputs needed for calculation
    :return rained_allocation_depth, irrigated_area, average_flow_rate:
    """
    rained_allocation_depth = validation.get_positive_num("Enter rationed allocation depth(D) in inches: ", 'float')

    irrigated_area = validation.get_positive_num("Enter area being irrigated(A) in acres: ", 'float')

    average_flow_rate = validation.get_positive_num("Enter average rate of flow(Q) in U.S. gpm: ", 'float')

    return rained_allocation_depth, irrigated_area, average_flow_rate


def calculations(rained_allocation_depth, irrigated_area, average_flow_rate):
    """
    Calculates the irrigation water allocation
    :param rained_allocation_depth:
    :param irrigated_area:
    :param average_flow_rate:
    :return irrigation_water_allocation:
    """
    # calculation for the irrigation water allocation
    irrigation_water_allocation = round(18.857 * rained_allocation_depth * irrigated_area / average_flow_rate, 1)
    return irrigation_water_allocation


def final_output(irrigation_water_allocation, irrigated_area, average_flow_rate, rained_allocation_depth):
    """
    Final output in sentence format
    :param irrigation_water_allocation:
    :param irrigated_area:
    :param average_flow_rate:
    :param rained_allocation_depth:
    :return:
    """
    # final print statement containing the inputs and final output all in one sentence
    print()
    print('The allocation of water will be used up in ' + str(round(irrigation_water_allocation, 1)) +
          ' days\nwhen ' + str(round(irrigated_area, 1)) + ' acres is irrigated with an ' +
          'irrigation system\nthat has a ' + str(round(average_flow_rate, 1)) + ' U.S. gpm system capacity ' +
          'and the rationed\nallocation depth is ' + str(round(rained_allocation_depth, 1)) + ' inches.')


# runs this specific module's main
if __name__ == "__main__":
    main()
