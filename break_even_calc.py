#!/usr/bin/env python3

# A simple cover crop calculator for Chapter 2's paired programming assignment assignment
# Programmers: Jordan Booth, Dan Peters, and Mackenzie Eskey
# Date: 2021.09.06

# display a program title
print("Break Even Calculator")
print("=" * 39)
print()

# get the estimated revenue
print("Estimate Revenue")
print("-" * 39)
crop_yield = float(input("Enter yield:\t"))
crop_price = float(input("Enter price:\t"))
gov_payment = float(input("Enter government payment:\t"))
print()

# calculate total cost
print("Estimate Revenue")
print("-" * 39)
variable_cost = float(input("Enter variable cost:\t"))
overhead_cost = float(input("Enter overhead_cost:\t"))


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
