#!/usr/bin/env python3

# A stocking rate calculator for Chapter 3's assignment
# Determines how many cow-calf pairs a pasture can support.
# Programmers: Jordan Booth
# Date: 2021.09.14

LINE_LENGTH = 60

print('Cow-Calf Pair Pasture Stocking Rates')
print('=' * LINE_LENGTH)

# while loop to get user input on the number of forage samples taken.
# only allows values 1-20
while True:
    forage_samples_taken = int(input('Enter the number of forage samples taken (1-20): '))

    if 0 < forage_samples_taken < 21:
        break
    else:
        print('Invalid value.')

print()
print("Please enter dry clipping samples in grams:")

clipping_sample_weight = 0

# for loop to get user input on sample weights in grams
# adds up to total weight of samples
for i in range(forage_samples_taken):
    clipping_sample_weight = clipping_sample_weight + int(input("Sample #" + str(i+1) + ": "))

print()

# calculating square foot average per pound and rounding it to the third decimal
square_foot_avg_lbs = round((clipping_sample_weight / forage_samples_taken) / 453.592, 3)

# calculating forage per acre and rounding it
forage_per_acre = round(square_foot_avg_lbs * 43560)

print('Square foot average per lb =', square_foot_avg_lbs)
print('Forage per acre in lbs =', forage_per_acre)
print()

# while loop to get user input on the utilization rate.
# only allows values 1-100
while True:
    utilization_rate = int(input('Enter the utilization rate (1-100): '))

    if 0 < utilization_rate < 101:
        break
    else:
        print('Invalid value.')

print()

# while loop to get user input on the animal unit month in lbs.
# only allows values 1-2000
while True:
    animal_unit_month = int(input('Enter the AUM (animal unit month) in lbs (1-2000): '))

    if 0 < animal_unit_month < 2001:
        break
    else:
        print('Invalid value.')

# calculating and rounding final stocking rate
stocking_rate = round((forage_per_acre * (utilization_rate/100)) / animal_unit_month, 2)

print()
print("Stocking rate (cow-calf per acre) =", stocking_rate)
print()
print("End of program")
