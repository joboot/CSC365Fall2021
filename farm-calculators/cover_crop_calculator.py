#!/usr/bin/env python3

"""
A simple cover crop calculator for Chapter 2's assignment
"""

import validation

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "9.28.2021"
__status__ = "Development"


def main():
    display_title()
    acreage_area = area_input()
    seeding_rate = seeding_input()
    cover_crop_needed = cover_crop_calc(acreage_area, seeding_rate)
    final_output(cover_crop_needed)


def display_title():
    """
    Displays title of program
    :return: none
    """
    # display a program title
    print("Cover Crop Calculator")
    validation.display_line()
    print()


def area_input():
    # get the estimated coverage area length and width in feet from the user
    print("Estimate Coverage Area")
    validation.display_line()
    area_length_ft = float(input("Enter length:\t"))
    area_width_ft = float(input("Enter width:\t"))
    print()

    # calculate acreage area
    acreage_area = (area_length_ft * area_width_ft)/43560
    print("Total Acreage Area =", acreage_area)
    print()
    return acreage_area


def seeding_input():
    # get estimated cover crop needed
    print("Estimate Cover Crop needed")
    validation.display_line()
    # get seeding rate from user
    seeding_rate = float(input("Enter seeding rate:\t"))
    return seeding_rate


def cover_crop_calc(acreage_area, seeding_rate):
    # calculate cover crop needed
    cover_crop_needed = seeding_rate * acreage_area
    return cover_crop_needed


def final_output(cover_crop_needed):
    # print cover crop needed
    print()
    print("Total cover crop needed:", cover_crop_needed)

    print()
    print("Goodbye")


# runs this specific module's main
if __name__ == "__main__":
    main()
