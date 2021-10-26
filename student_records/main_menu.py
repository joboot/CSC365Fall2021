"""
Student Data System for managing student information (student id, first name, and last name)
This module contains the functions for displaying the main menu and running the menu options
"""

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.21.2021"
__status__ = "Development"

import utils
import student_maintenance


def main():
    students = []
    next_student_id = 0

    while True:
        display_menu()

        menu_input = utils.get_range('Please enter a valid menu # (0-4): ', -1, 4, 'int')
        print()
        if menu_input == 1:
            print("List all students")
            utils.display_line()
            student_maintenance.list_students(students)

        elif menu_input == 2:
            next_student_id += 1
            print("Add a student")
            utils.display_line()
            student_maintenance.add_student(students, next_student_id)

        elif menu_input == 3:
            print("Update a student")
            utils.display_line()
            student_maintenance.update_student(students)

        elif menu_input == 4:
            print("Delete a student")
            utils.display_line()
            student_maintenance.delete_student(students)

        elif menu_input == 0:
            print("Exit program")
            break
        print()


def display_menu():
    print('Student Menu')
    utils.display_line()
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Update a student')
    print('4 - Delete a student')
    print('0 - Exit program')


# runs this specific module's main
if __name__ == "__main__":
    main()
