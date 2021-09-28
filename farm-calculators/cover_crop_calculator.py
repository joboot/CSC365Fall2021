#!/usr/bin/env python3

"""
A simple cover crop calculator for Chapter 2's assignment
"""

import validation

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "9.28.2021"
__status__ = "Development"

LINE_LENGTH = 60

# display a program title
print("Cover Crop Calculator")
print("=" * LINE_LENGTH)
print()

# get the estimated coverage area length and width in feet from the user
print("Estimate Coverage Area")
print("-" * 39)
area_length_ft = float(input("Enter length:\t"))
area_width_ft = float(input("Enter width:\t"))
print()

# calculate acreage area
acreage_area = (area_length_ft * area_width_ft)/43560
print("Total Acreage Area =", acreage_area)
print()

# get estimated cover crop needed
print("Estimate Cover Crop needed")
print("-" * LINE_LENGTH)
# get seeding rate from user
seeding_rate = float(input("Enter seeding rate:\t"))

# calculate cover crop needed
cover_crop_needed = seeding_rate * acreage_area

# print cover crop needed
print()
print("Total cover crop needed:", cover_crop_needed)

print()
print("Goodbye")
