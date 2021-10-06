#!/usr/bin/env python3

"""
A simple Break Even calculator for Chapter 2's paired programming assignment
Calculates the break even price and displays a table with variations in cost and yield
"""

import validation

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "9.30.2021"
__status__ = "Development"


def main():
    """
    Inputs:
    Crop yield
    Crop price
    Government payment
    Variable cost
    Overhead cost

    Outputs:
    Increased and decreased cost values and calculations
    Increased and decreased yield values and calculations
    Final output table with all information
    :return: n/a
    """
    display_title()

    crop_yield, crop_price, gov_payment, variable_cost, overhead_cost = user_input()

    std_total_revenue, std_total_cost, std_earnings, std_break_even_price, std_per_bushel_profit = \
        calculate_std_output(crop_yield, crop_price, gov_payment, variable_cost, overhead_cost)

    dc_crop_yield, dc_variable_cost, dc_overhead_cost, dc_total_revenue, dc_total_cost, \
    dc_earnings, dc_break_even_price, dc_per_bushel_profit = \
        calculate_dc_output(crop_yield, crop_price, gov_payment, variable_cost, overhead_cost)

    ic_crop_yield, ic_variable_cost, ic_overhead_cost, ic_total_revenue, ic_total_cost, \
    ic_earnings, ic_break_even_price, ic_per_bushel_profit = \
        calculate_ic_output(crop_yield, crop_price, gov_payment, variable_cost, overhead_cost)

    dy_crop_yield, dy_variable_cost, dy_overhead_cost, dy_total_revenue, dy_total_cost, \
    dy_earnings, dy_break_even_price, dy_per_bushel_profit = \
        calculate_dy_output(crop_yield, crop_price, gov_payment, variable_cost, overhead_cost)

    iy_crop_yield, iy_variable_cost, iy_overhead_cost, iy_total_revenue, iy_total_cost, \
    iy_earnings, iy_break_even_price, iy_per_bushel_profit = \
        calculate_iy_output(crop_yield, crop_price, gov_payment, variable_cost, overhead_cost)

    table_output(crop_yield, crop_price, gov_payment, variable_cost, overhead_cost,
                 std_total_revenue, std_total_cost, std_earnings, std_break_even_price, std_per_bushel_profit,
                 dc_crop_yield, dc_variable_cost, dc_overhead_cost, dc_total_revenue, dc_total_cost,
                 dc_earnings, dc_break_even_price, dc_per_bushel_profit,
                 ic_crop_yield, ic_variable_cost, ic_overhead_cost, ic_total_revenue, ic_total_cost,
                 ic_earnings, ic_break_even_price, ic_per_bushel_profit,
                 dy_crop_yield, dy_variable_cost, dy_overhead_cost, dy_total_revenue, dy_total_cost,
                 dy_earnings, dy_break_even_price, dy_per_bushel_profit,
                 iy_crop_yield, iy_variable_cost, iy_overhead_cost, iy_total_revenue, iy_total_cost,
                 iy_earnings, iy_break_even_price, iy_per_bushel_profit
                 )

    print('Break Even Calculator has ended.')


def display_title():
    """
    Displays program title
    :return:
    """
    # display a program title
    print("Break Even Calculator")
    validation.display_line()
    print()


def user_input():
    """
    Gets user input needed for pricing and cost
    :return crop_yield, crop_price, gov_payment, variable_cost, overhead_cost:
    """
    # get the per acre information
    print("Enter per acre information")
    validation.display_line()
    crop_yield = validation.get_positive_num("Enter yield: ", 'float')
    crop_price = validation.get_positive_num("Enter price: ", 'float')
    gov_payment = validation.get_positive_num("Enter Government Payment: ", 'float')
    variable_cost = validation.get_positive_num("Enter Variable Cost: ", 'float')
    overhead_cost = validation.get_positive_num("Enter Overhead Cost: ", 'float')
    print()
    return crop_yield, crop_price, gov_payment, variable_cost, overhead_cost


def calculate_std_output(crop_yield, crop_price, gov_payment, variable_cost, overhead_cost):
    """
    Calculate the outputs in standard condition
    :param crop_yield: Base crop yield
    :param crop_price: Base crop price
    :param gov_payment: Base government payment
    :param variable_cost: Base variable cost
    :param overhead_cost: Base overhead cost
    :return std_total_revenue, std_total_cost, std_earnings, std_break_even_price, std_per_bushel_profit:
    """
    std_total_revenue = ((crop_yield * crop_price) + gov_payment)
    std_total_cost = (variable_cost + overhead_cost)
    std_earnings = (std_total_cost - std_total_revenue)
    std_break_even_price = ((std_total_cost - gov_payment) / crop_yield)
    std_per_bushel_profit = (std_break_even_price - crop_price)
    return std_total_revenue, std_total_cost, std_earnings, std_break_even_price, std_per_bushel_profit


def calculate_dc_output(crop_yield, crop_price, gov_payment, variable_cost, overhead_cost):
    """
    Calculate the outputs when 10% decrease in costs
    :param crop_yield: Base crop yield
    :param crop_price: Base crop price
    :param gov_payment: Base government payment
    :param variable_cost: Base variable cost
    :param overhead_cost: Base overhead cost
    :return dc_crop_yield, dc_variable_cost, dc_overhead_cost, dc_total_revenue, dc_total_cost,
           dc_earnings, dc_break_even_price, dc_per_bushel_profit:
    """
    dc_crop_yield = crop_yield
    dc_variable_cost = (variable_cost * 0.9)
    dc_overhead_cost = (overhead_cost * 0.9)
    dc_total_revenue = ((dc_crop_yield * crop_price) + gov_payment)
    dc_total_cost = (dc_variable_cost + dc_overhead_cost)
    dc_earnings = (dc_total_cost - dc_total_revenue)
    dc_break_even_price = ((dc_total_cost - gov_payment) / dc_crop_yield)
    dc_per_bushel_profit = (dc_break_even_price - crop_price)
    return dc_crop_yield, dc_variable_cost, dc_overhead_cost, dc_total_revenue, dc_total_cost, \
           dc_earnings, dc_break_even_price, dc_per_bushel_profit


def calculate_ic_output(crop_yield, crop_price, gov_payment, variable_cost, overhead_cost):
    """
    Calculate the outputs when 10% increase in costs
    :param crop_yield: Base crop yield
    :param crop_price: Base crop price
    :param gov_payment: Base government payment
    :param variable_cost: Base variable cost
    :param overhead_cost: Base overhead cost
    :return ic_crop_yield, ic_variable_cost, ic_overhead_cost, ic_total_revenue, ic_total_cost,
           ic_earnings, ic_break_even_price, ic_per_bushel_profit:
    """
    ic_crop_yield = crop_yield
    ic_variable_cost = (variable_cost * 1.1)
    ic_overhead_cost = (overhead_cost * 1.1)
    ic_total_revenue = ((ic_crop_yield * crop_price) + gov_payment)
    ic_total_cost = (ic_variable_cost + ic_overhead_cost)
    ic_earnings = (ic_total_cost - ic_total_revenue)
    ic_break_even_price = ((ic_total_cost - gov_payment) / ic_crop_yield)
    ic_per_bushel_profit = (ic_break_even_price - crop_price)
    return ic_crop_yield, ic_variable_cost, ic_overhead_cost, ic_total_revenue, ic_total_cost, \
           ic_earnings, ic_break_even_price, ic_per_bushel_profit


def calculate_dy_output(crop_yield, crop_price, gov_payment, variable_cost, overhead_cost):
    """
    Calculate the outputs when 10% decrease in yield
    :param crop_yield: Base crop yield
    :param crop_price: Base crop price
    :param gov_payment: Base government payment
    :param variable_cost: Base variable cost
    :param overhead_cost: Base overhead cost
    :return dy_crop_yield, dy_variable_cost, dy_overhead_cost, dy_total_revenue, dy_total_cost,
           dy_earnings, dy_break_even_price, dy_per_bushel_profit:
    """
    dy_crop_yield = (crop_yield * 0.9)
    dy_variable_cost = variable_cost
    dy_overhead_cost = overhead_cost
    dy_total_revenue = ((dy_crop_yield * crop_price) + gov_payment)
    dy_total_cost = (dy_variable_cost + dy_overhead_cost)
    dy_earnings = (dy_total_cost - dy_total_revenue)
    dy_break_even_price = ((dy_total_cost - gov_payment) / dy_crop_yield)
    dy_per_bushel_profit = (dy_break_even_price - crop_price)
    return dy_crop_yield, dy_variable_cost, dy_overhead_cost, dy_total_revenue, dy_total_cost, \
           dy_earnings, dy_break_even_price, dy_per_bushel_profit


def calculate_iy_output(crop_yield, crop_price, gov_payment, variable_cost, overhead_cost):
    """
    Calculate the outputs when 10% increase in yield
    :param crop_yield: Base crop yield
    :param crop_price:
    :param gov_payment:
    :param variable_cost:
    :param overhead_cost:
    :return iy_crop_yield, iy_variable_cost, iy_overhead_cost, iy_total_revenue, iy_total_cost,
           iy_earnings, iy_break_even_price, iy_per_bushel_profit:
    """
    iy_crop_yield = (crop_yield * 1.1)
    iy_variable_cost = variable_cost
    iy_overhead_cost = overhead_cost
    iy_total_revenue = ((iy_crop_yield * crop_price) + gov_payment)
    iy_total_cost = (iy_variable_cost + iy_overhead_cost)
    iy_earnings = (iy_total_cost - iy_total_revenue)
    iy_break_even_price = ((iy_total_cost - gov_payment) / iy_crop_yield)
    iy_per_bushel_profit = (iy_break_even_price - crop_price)
    return iy_crop_yield, iy_variable_cost, iy_overhead_cost, iy_total_revenue, iy_total_cost, \
           iy_earnings, iy_break_even_price, iy_per_bushel_profit


def table_output(crop_yield, crop_price, gov_payment, variable_cost, overhead_cost,
                 std_total_revenue, std_total_cost, std_earnings, std_break_even_price, std_per_bushel_profit,
                 dc_crop_yield, dc_variable_cost, dc_overhead_cost, dc_total_revenue, dc_total_cost,
                 dc_earnings, dc_break_even_price, dc_per_bushel_profit,
                 ic_crop_yield, ic_variable_cost, ic_overhead_cost, ic_total_revenue, ic_total_cost,
                 ic_earnings, ic_break_even_price, ic_per_bushel_profit,
                 dy_crop_yield, dy_variable_cost, dy_overhead_cost, dy_total_revenue, dy_total_cost,
                 dy_earnings, dy_break_even_price, dy_per_bushel_profit,
                 iy_crop_yield, iy_variable_cost, iy_overhead_cost, iy_total_revenue, iy_total_cost,
                 iy_earnings, iy_break_even_price, iy_per_bushel_profit
                 ):
    """
    Creation of table formatting headers and output
    :param crop_yield: Base crop yield
    :param crop_price: Base crop price
    :param gov_payment: Base government aid
    :param variable_cost: Base variable cost
    :param overhead_cost: Base overhead cost
    :param std_total_revenue: Base total revenue
    :param std_total_cost: Base total cost
    :param std_earnings: Base earnings
    :param std_break_even_price: Base break even price
    :param std_per_bushel_profit: Base per bushel profit
    :param dc_crop_yield: Decreased cost crop yield
    :param dc_variable_cost: Decreased cost variable cost
    :param dc_overhead_cost: Decreased cost overhead cost
    :param dc_total_revenue: Decreased cost total revenue
    :param dc_total_cost: Decreased cost total cost
    :param dc_earnings: Decreased cost earnings
    :param dc_break_even_price: Decreased cost break even price
    :param dc_per_bushel_profit: Decreased cost per bushel profit
    :param ic_crop_yield: Increased cost crop yield
    :param ic_variable_cost: Increased cost variable cost
    :param ic_overhead_cost: Increased cost overhead cost
    :param ic_total_revenue: Increased cost total revenue
    :param ic_total_cost: Increased cost total cost
    :param ic_earnings: Increased cost earnings
    :param ic_break_even_price: Increased cost break even price
    :param ic_per_bushel_profit: Increased cost per bushel profit
    :param dy_crop_yield: Decreased yield crop yield
    :param dy_variable_cost: Decreased yield variable cost
    :param dy_overhead_cost: Decreased yield overhead cost
    :param dy_total_revenue: Decreased yield total revenue
    :param dy_total_cost: Decreased yield total cost
    :param dy_earnings: Decreased yield earnings
    :param dy_break_even_price: Decreased yield break even price
    :param dy_per_bushel_profit: Decreased yield per bushel profit
    :param iy_crop_yield: Increased yield crop yield
    :param iy_variable_cost: Increased yield variable cost
    :param iy_overhead_cost: Increased yield overhead cost
    :param iy_total_revenue: Increased yield total revenue
    :param iy_total_cost: Increased yield total cost
    :param iy_earnings: Increased yield earnings
    :param iy_break_even_price: Increased yield break even price
    :param iy_per_bushel_profit: Increased yield per bushel profit
    :return: n/a
    """

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

    print(f'{"-" * 20:>20s}'
          f'{"-" * 13:>15s}'
          f'{"-" * 13:>15s}'
          f'{"-" * 13:>15s}'
          f'{"-" * 13:>15s}'
          f'{"-" * 13:>15s}')

    print(f'{"Yield":20s}'
          f'{crop_yield:15,.2f}'
          f'{dy_crop_yield:15,.2f}'
          f'{iy_crop_yield:15,.2f}'
          f'{dc_crop_yield:15,.2f}'
          f'{ic_crop_yield:15,.2f}')

    print(f'{"Price":20s}'
          f'{crop_price:15,.2f}'
          f'{crop_price:15,.2f}'
          f'{crop_price:15,.2f}'
          f'{crop_price:15,.2f}'
          f'{crop_price:15,.2f}')

    print(f'{"Government Payment":20s}'
          f'{gov_payment:15,.2f}'
          f'{gov_payment:15,.2f}'
          f'{gov_payment:15,.2f}'
          f'{gov_payment:15,.2f}'
          f'{gov_payment:15,.2f}')

    print(f'{"Total Revenue":20s}'
          f'{std_total_revenue:15,.2f}'
          f'{dy_total_revenue:15,.2f}'
          f'{iy_total_revenue:15,.2f}'
          f'{dc_total_revenue:15,.2f}'
          f'{ic_total_revenue:15,.2f}')

    print()

    print(f'{"Variable Cost":20s}'
          f'{variable_cost:15,.2f}'
          f'{dy_variable_cost:15,.2f}'
          f'{iy_variable_cost:15,.2f}'
          f'{dc_variable_cost:15,.2f}'
          f'{ic_variable_cost:15,.2f}')

    print(f'{"Overhead Cost":20s}'
          f'{overhead_cost:15,.2f}'
          f'{dy_overhead_cost:15,.2f}'
          f'{iy_overhead_cost:15,.2f}'
          f'{dc_overhead_cost:15,.2f}'
          f'{ic_overhead_cost:15,.2f}')

    print(f'{"Total Cost":20s}'
          f'{std_total_cost:15,.2f}'
          f'{dy_total_cost:15,.2f}'
          f'{iy_total_cost:15,.2f}'
          f'{dc_total_cost:15,.2f}'
          f'{ic_total_cost:15,.2f}')

    print()

    print(f'{"Earnings":20s}'
          f'{std_earnings:15,.2f}'
          f'{dy_earnings:15,.2f}'
          f'{iy_earnings:15,.2f}'
          f'{dc_earnings:15,.2f}'
          f'{ic_earnings:15,.2f}')

    print()

    print(f'{"Break-even Price":20s}'
          f'{std_break_even_price:15,.2f}'
          f'{dy_break_even_price:15,.2f}'
          f'{iy_break_even_price:15,.2f}'
          f'{dc_break_even_price:15,.2f}'
          f'{ic_break_even_price:15,.2f}')

    print(f'{"Per Bushel Profit":20s}'
          f'{std_per_bushel_profit:15,.2f}'
          f'{dy_per_bushel_profit:15,.2f}'
          f'{iy_per_bushel_profit:15,.2f}'
          f'{dc_per_bushel_profit:15,.2f}'
          f'{ic_per_bushel_profit:15,.2f}')


# runs this specific module's main
if __name__ == "__main__":
    main()
