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

LINE_LENGTH = 60

# Program header (Mackenzie)
print('Irrigation Water Allocations Calculator')
print('=' * LINE_LENGTH)

user_input = 'y'

# While loop intakes user input on whether or not they would like to calculate (Mackenzie)
while user_input.lower() == 'y':

    # While true loop for rationed allocation depth input (Mackenzie)
    while True:
        rained_allocation_depth = float(input(f'{"Enter rationed allocation depth(D) in inches: ":>56}'))

        # if it is less than 0, it is invalid
        if 0 < rained_allocation_depth:
            break
        else:
            print(f'{"Invalid value. Please enter again.":>55}')

    # while true loop for area being irrigated input (Jordan)
    while True:
        irrigated_area = float(input(f'{"Enter area being irrigated(A) in acres: ":>56}'))

        # if it is less than 0, it is invalid
        if 0 < irrigated_area:
            break
        else:
            print(f'{"Invalid value. Please enter again.":>55}')

    # while true loop for average rate of flow input (Jordan)
    while True:
        average_flow_rate = float(input(f'{"Enter average rate of flow(Q) in U.S. gpm: ":>56}'))

        # if it is less than 0, it is invalid
        if 0 < average_flow_rate:
            break
        else:
            print(f'{"Invalid value. Please enter again.":>55}')

    # calculation for the irrigation water allocation (Mackenzie)
    irrigation_water_allocation = round(18.857 * rained_allocation_depth * irrigated_area / average_flow_rate, 1)

    # final print statement containing the inputs and final output all in one sentence (Jordan)
    print()
    print('The allocation of water will be used up in ' + str(irrigation_water_allocation) +
          ' days\nwhen ' + str(round(irrigated_area)) + ' acres is irrigated with an ' +
          'irrigation system\nthat has a ' + str(round(average_flow_rate)) + ' U.S. gpm system capacity ' +
          'and the rationed\nallocation depth is ' + str(round(rained_allocation_depth)) + ' inches.')

    # ask user if they would like to make another calculation, if not, break out of main while loop (Jordan)
    print()
    user_input = input('Would you like to make another calculation?(y/n): ')
    print()
    print('=' * LINE_LENGTH)

print('Program has ended.')
