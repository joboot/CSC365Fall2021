#!/usr/bin/env python3

# A simple cover crop calculator for Chapter 2's paired programming assignment assignment
# Programmers: Jordan Booth, Dan Peters, and Mackenzie Eskey
# Date: 2021.09.06

# display a program title (Jordan)
print("Break Even Calculator")
print("=" * 39)
print()

# get the estimated revenue (Jordan)
print("Enter per acre information")
print("-" * 39)
crop_yield = float(input(f'{"Enter yield: ":>35s}'))
crop_price = float(input(f'{"Enter price: ":>35s}'))
gov_payment = float(input(f'{"Enter Government Payment: ":>35s}'))
variable_cost = float(input(f'{"Enter Variable Cost: ":>35s}'))
overhead_cost = float(input(f'{"Enter Overhead Cost: ":>35s}'))
print()

# calculate the outputs in standard condition for total revenue,
# total costs, earnings, break even price, and per bushel profit (Mackenzie)
# std_total_revenue = ((crop_yield * crop_price) + gov_payment)
# std_total_cost = (variable_cost + overhead_cost)
# std_earnings = (dc_total_revenue - dc_total_cost)
# std_break_even_price = ((dc_total_cost - gov_payment)/crop_yield)
# std_per_bushel_profit = (crop_price - dc_break_even_price)
#
# # calculate the outputs when 10% decrease in yield for total revenue,
# # total costs, earnings, break even price, and per bushel profit (Mackenzie)
# dy_total_revenue = ((crop_yield * crop_price) + gov_payment)
# dy_total_cost = (variable_cost + overhead_cost)
# dy_earnings = (dc_total_revenue - dc_total_cost)
# dy_break_even_price = ((dc_total_cost - gov_payment)/crop_yield)
# dy_per_bushel_profit = (crop_price - dc_break_even_price)


# calculate the outputs when 10% increase in yield for total revenue,
# total costs, earnings, break even price, and per bushel profit (Mackenzie)

# calculate the outputs when 10% decrease in costs for total revenue,
# total costs, earnings, break even price, and per bushel profit (Mackenzie)
dc_total_revenue = ((crop_yield * crop_price) + gov_payment)
dc_total_cost = ((variable_cost + overhead_cost) * 0.9)
dc_earnings = (dc_total_revenue - dc_total_cost)
dc_break_even_price = ((dc_total_cost - gov_payment)/crop_yield)
dc_per_bushel_profit = (crop_price - dc_break_even_price)

# calculate the outputs when 10% increase in costs for total revenue,
# total costs, earnings, break even price, and per bushel profit (Mackenzie)
ic_total_revenue = ((crop_yield * crop_price) + gov_payment)
ic_total_cost = ((variable_cost + overhead_cost) * 1.1)
ic_earnings = (ic_total_revenue - ic_total_cost)
ic_break_even_price = ((ic_total_cost - gov_payment)/crop_yield)
ic_per_bushel_profit = (crop_price - ic_break_even_price)

dy_per_bushel_profit = 2
iy_per_bushel_profit = 3

# formatting headers (provided by Debbie, typed by Mackenzie)
print(f'{"":20s}'
      f'{"":15s}'
      f'{"10% Decrease":>15s}'
      f'{"10% Increase":>15s}'
      f'{"10% Decrease":>15s}'
      f'{"10% Increase":>15s}')

print(f'{"BreakEven Calculator":20s}'
      f'{"Per Acre":>15s}'  
      f'{"in Yield":>15s}'
      f'{"in Yield":>15s}'
      f'{"in Cost":>15s}'
      f'{"in Cost":>15s}')

print(f'{"-"*20:>20s}'
      f'{"-"*13:>15s}'
      f'{"-"*13:>15s}'
      f'{"-"*13:>15s}'
      f'{"-"*13:>15s}'
      f'{"-"*13:>15s}')

print(f'{"Yield":20s}'
      f'{crop_yield:15,.2f}'
      f'{dy_per_bushel_profit:15,.2f}'
      f'{iy_per_bushel_profit:15,.2f}'
      f'{dc_per_bushel_profit:15,.2f}'
      f'{ic_per_bushel_profit:15,.2f}')

print(f'{"Price":20s}'
      f'{crop_price}'
      f'{crop_price:15,.2f}'
      f'{crop_price:15,.2f}'
      f'{crop_price:15,.2f}'
      f'{crop_price:15,.2f}')

print(f'{"Government Payment":20s}'
      f'{gov_payment}'
      f'{gov_payment:15,.2f}'
      f'{gov_payment:15,.2f}'
      f'{gov_payment:15,.2f}'
      f'{gov_payment:15,.2f}')

# print(f'{"Total Revenue":20s}'
#       f'{total_revenue}'
#       f'{dy_total_revenue:15,.2f}'
#       f'{iy_total_revenue:15,.2f}'
#       f'{dc_total_revenue:15,.2f}'
#       f'{ic_total_revenue:15,.2f}')
#
# print()
#
# print(f'{"Variable Cost":20s}'
#       f'{variable_cost}'
#       f'{dy_variable_cost:15,.2f}'
#       f'{iy_variable_cost:15,.2f}'
#       f'{dc_variable_cost:15,.2f}'
#       f'{ic_variable_cost:15,.2f}')
#
# print(f'{"Overhead Cost":20s}'
#       f'{overhead_cost}'
#       f'{dy_overhead_cost:15,.2f}'
#       f'{iy_overhead_cost:15,.2f}'
#       f'{dc_overhead_cost:15,.2f}'
#       f'{ic_overhead_cost:15,.2f}')
#
# print(f'{"Total Cost":20s}'
#       f'{}'
#       f'{dy_overhead_cost:15,.2f}'
#       f'{iy_overhead_cost:15,.2f}'
#       f'{dc_overhead_cost:15,.2f}'
#       f'{ic_overhead_cost:15,.2f}')
# print()
#
# print(f'{"Earnings":20s}'
#
# print()
#
# print(f'{"Break-even Price":20s}'
#
# print(f'{"Per Bushel Profit":20s}'
#       f'{per_bushel_profit:15,.2f}'
#       f'{dy_per_bushel_profit:15,.2f}'
#       f'{iy_per_bushel_profit:15,.2f}'
#       f'{dc_per_bushel_profit:15,.2f}'
#       f'{ic_per_bushel_profit:15,.2f}')

print()
print("Goodbye")
