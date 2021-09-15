#!/usr/bin/env python3

# A calculator to determine how many cow-calf pairs a pasture can support per acre of forage.
# Programmers: Mackenzie Eskey
# Date: 9-14-2021

# initialize variables
counter = 0
weight_total = 0
sample_weight = 0

# print header of program
print('Cow-Calf Pair Pasture Stocking Rates')
print('=' * 55)

# while loop to get user input for the amount of samples taken
while True:
    forage_samples_taken = int(input('Enter the number of forage samples taken (Valid 1-20): '))
    if 0 < forage_samples_taken < 21:
        break
    else:
        print('Invalid value.')

print()

print('Please enter dry clipping samples in grams')
print('-' * 55)

# for loop to get user input for weight of each sample
for i in range(forage_samples_taken):
    sample_weight = int(input('Sample #' + str(i + 1) + ': '))
    if 0 <= sample_weight <= 1000:
        weight_total += sample_weight
        counter += 1
    else:
        print("Invalid value.")

print()

# calculation and print statement for the square foot average per pound
square_foot_avg_lbs = round((weight_total / forage_samples_taken) / 453.592, 3)
print('Square foot avg per pound = ' + str(square_foot_avg_lbs))

# calculation and print statement for the forage per acre in pounds
forage_per_acre = round(square_foot_avg_lbs * 43560)
print('Forage per acre in pounds = ' + str(forage_per_acre))

print()

# while loop to get user input for utilization rate
while True:
    utilization_rate = int(input('Enter the utilization rate (Valid 1-100): '))
    if 0 < utilization_rate < 101:
        break
    else:
        print('Invalid value.')

# while loop to get user input for animal unit month
while True:
    animal_unit_month = int(input('Enter the AUM (Valid 1-2000): '))
    if 0 < animal_unit_month < 2001:
        break
    else:
        print('Invalid value.')

print()

# calculation and print statement for the stocking rate
stocking_rate = round((forage_per_acre * (utilization_rate / 100)) / animal_unit_month, 2)
print('Stocking rate (cow-calf per acre) = ' + str(stocking_rate))

print()

print('Goodbye!')
