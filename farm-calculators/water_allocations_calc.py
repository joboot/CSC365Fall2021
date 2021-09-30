#!/usr/bin/env python3

"""
A irrigation water allocations calculator for paired programming assignment 2
This program calculates and determines how long it will take to use up an allocation of water for irrigation.
"""

import validation

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "9.28.2021"
__status__ = "Development"


def main():
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
    print('Program has ended.')


def display_title():
    # Program header
    print('Irrigation Water Allocations Calculator')
    validation.display_line()


def user_inputs():
    # While true loop for rationed allocation depth input
    while True:
        rained_allocation_depth = float(input(f'{"Enter rationed allocation depth(D) in inches: ":>56}'))

        # if it is less than 0, it is invalid
        if 0 < rained_allocation_depth:
            break
        else:
            print(f'{"Invalid value. Please enter again.":>55}')

    # while true loop for area being irrigated input
    while True:
        irrigated_area = float(input(f'{"Enter area being irrigated(A) in acres: ":>56}'))

        # if it is less than 0, it is invalid
        if 0 < irrigated_area:
            break
        else:
            print(f'{"Invalid value. Please enter again.":>55}')

    # while true loop for average rate of flow input
    while True:
        average_flow_rate = float(input(f'{"Enter average rate of flow(Q) in U.S. gpm: ":>56}'))

        # if it is less than 0, it is invalid
        if 0 < average_flow_rate:
            break
        else:
            print(f'{"Invalid value. Please enter again.":>55}')
    return rained_allocation_depth, irrigated_area, average_flow_rate


def calculations(rained_allocation_depth, irrigated_area, average_flow_rate):
    # calculation for the irrigation water allocation
    irrigation_water_allocation = round(18.857 * rained_allocation_depth * irrigated_area / average_flow_rate, 1)
    return irrigation_water_allocation


def final_output(irrigation_water_allocation, irrigated_area, average_flow_rate, rained_allocation_depth):
    # final print statement containing the inputs and final output all in one sentence
    print()
    print('The allocation of water will be used up in ' + str(irrigation_water_allocation) +
          ' days\nwhen ' + str(round(irrigated_area)) + ' acres is irrigated with an ' +
          'irrigation system\nthat has a ' + str(round(average_flow_rate)) + ' U.S. gpm system capacity ' +
          'and the rationed\nallocation depth is ' + str(round(rained_allocation_depth)) + ' inches.')

    # ask user if they would like to make another calculation, if not, break out of main while loop
    print()
    user_input = input('Would you like to make another calculation?(y/n): ')
    print()
    validation.display_line()


# runs this specific module's main
if __name__ == "__main__":
    main()
