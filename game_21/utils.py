"""
Utility code and validation code for output and data input from the user.
"""

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "11.30.2021"
__status__ = "Development"


def main():
    """
    Test each function to see if they work correctly
    :return: n/a
    """
    display_line()


def display_line():
    """
    Displays a line for program output
    :return: n/a
    """
    line_length = 60
    print('=' * line_length)


def get_yn(prompt):
    """
    Prompt user for input
    :param prompt: Text to ask the user for input
    :return: Answer input by the user
    """
    while True:
        user_input = input(prompt)
        user_input = user_input.lower()
        if user_input == 'y' or user_input == 'yes':
            return True

        elif user_input == 'n' or user_input == 'no':
            return False

        else:
            print('Please enter y = Yes, n = No.')


# runs this specific module's main
if __name__ == "__main__":
    main()
