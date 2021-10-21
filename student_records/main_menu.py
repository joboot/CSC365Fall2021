"""
Student Data System for managing student information (student id, first name, and last name)
This module contains the functions for displaying the main menu and running the menu options
"""

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.21.2021"
__status__ = "Development"

import utils


def display_menu():
    print('Student Menu')
    utils.display_line()
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Update a student')
    print('4 - Delete a student')
    print('0 - Exit program')


