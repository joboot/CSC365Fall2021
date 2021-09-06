#!/usr/bin/env python3

# A simple cover crop calculator for Chapter 2's assignment
# Programmer: Jordan Booth
# Date: 2021.09.06

# display a program title
print("Cover Crop Calculator")
print("=" * 39)
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
print("-" * 39)
# get seeding rate from user
seeding_rate = float(input("Enter seeding rate:\t"))

# calculate cover crop needed
cover_crop_needed = seeding_rate * acreage_area

# print cover crop needed
print()
print("Total cover crop needed:", cover_crop_needed)

print()
print("Goodbye")
