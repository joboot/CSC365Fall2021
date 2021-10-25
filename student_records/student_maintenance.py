"""
Student maintenance module
"""

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.21.2021"
__status__ = "Development"


def main():
    print('this is main of student maintenance.')


def add_student(students, next_student_id):
    """
    Display the all student information stored in a 2D list.  It will increment the last student id by one
    and use it as the new student's id.  It also, displays that the student was successfully added.

    :param students: student data (id, first_name, last_name)
    :type students: 2d list

    :param next_student_id: the next student id to be used for the add function
    :type next_student_id: int

    :return no value
    :rtype none
    :return:
    """


def delete_student(students):
    """
    It will first check to see if there is any student data, and notify the user if no data is found.

    It will then prompt the user for a valid student ID to be deleted from the 2D list
    It handles for non numeric data, and student IDs that do not exists via the find_student_index

    It will prompt the user to confirm they want to delete the selected student, and then let the user know
    if the user was successfully deleted.

    :param students: student data (id, first_name, last_name)
    :type students: 2d list

    :return no value
    :rtype none
    """


def find_student_index(students, student_id):
    """
    Search the 2D list for a specific student ID.
    CODE EXAMPLE:
    for student in students:
        if student_id in student:
            return students.index(student)
    return -1
    :param students: student data (id, first_name, last_name)
    :type students: 2d list
    :param student_id: student id that they user wants to find
    :type student_id: int

    :return the index of the student in the 2D list or -1 if not found
    :rtype int
    """


def list_students(students):
    """
    Display the all student information stored in a 2D list (id, first name, last name)
    It will notify the student if there is no data found.

    :param students: student data (id, first_name, last_name)
    :type students: 2d list

    :return no value
    :rtype none
    """


def update_student(students):
    """
    It will first check to see if there is any student data, and notify the user if no data is found.

    It will then prompt the user for a valid student ID to be updated from the 2D list
    It handles for non numeric data, and student IDs that do not exists via the find_student_index

    It will prompt the user to confirm they want to update the selected student, and then let the user know
    if the user was successfully updated.

    :param students: student data (id, first_name, last_name)
    :type students: 2d list

    :return no value
    :rtype none
    """


# runs this specific module's main
if __name__ == "__main__":
    main()
