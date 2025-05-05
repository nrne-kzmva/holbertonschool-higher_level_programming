#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order"""
    if my_list:  # Check if the list is not empty
        for i in reversed(my_list):  # Iterate through the list in reverse
            print("{:d}".format(i))  # Print each integer as a decimal number
