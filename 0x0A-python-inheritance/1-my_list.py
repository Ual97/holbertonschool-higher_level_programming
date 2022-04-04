#!/usr/bin/python3
"""
Module 1-my_list

inherits from class list
"""


class MyList(list):
    """inherits from class list"""
    def print_sorted(self):
        """prints list of ints in ascending order"""
        print(sorted(self))
