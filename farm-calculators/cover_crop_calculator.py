#!/usr/bin/env python3

"""
A simple cover crop calculator for Chapter 2's assignment
"""

import validation

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "9.30.2021"
__status__ = "Development"


def main():
    """
    Main function, runs whole program
    :return:
    """
    display_title()
    acreage_area = area_input()
    seeding_rate = seeding_input()
    cover_crop_needed = cover_crop_calc(acreage_area, seeding_rate)
    final_output(cover_crop_needed)
    print('Cover Crop Calculator has ended.')


def display_title():
    """
    Displays title of program
    :return:
    """
    # display a program title
    print("Cover Crop Calculator")
    validation.display_line()
    print()


def area_input():
    """
    Estimates area of land in acres
    :return acreage_area:
    """
    # get the estimated coverage area length and width in feet from the user
    print("Estimate Coverage Area")
    validation.display_line()
    area_length_ft = validation.get_positive_num("Enter length:\t", 'float')
    area_width_ft = validation.get_positive_num("Enter width:\t", 'float')
    print()

    # calculate acreage area
    acreage_area = (area_length_ft * area_width_ft)/43560
    print("Total Acreage Area =", round(acreage_area, 3))
    print()
    return acreage_area


def seeding_input():
    """
    Gets user input on seeding rate
    :return seeding_rate:
    """
    # get estimated cover crop needed
    print("Estimate Cover Crop needed")
    validation.display_line()
    # get seeding rate from user
    seeding_rate = validation.get_positive_num("Enter seeding rate:\t", 'float')
    return seeding_rate


def cover_crop_calc(acreage_area, seeding_rate):
    """
    Calculates cover crop needed
    :param acreage_area:
    :param seeding_rate:
    :return cover_crop_needed:
    """
    # calculate cover crop needed
    cover_crop_needed = seeding_rate * acreage_area
    return cover_crop_needed


def final_output(cover_crop_needed):
    """
    Final output of cover crop needed
    :param cover_crop_needed:
    :return:
    """
    # print cover crop needed
    print()
    print("Total cover crop needed:", round(cover_crop_needed, 3))


# runs this specific module's main
if __name__ == "__main__":
    main()
