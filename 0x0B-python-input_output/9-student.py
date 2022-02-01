#!/usr/bin/python3
"""
class Student that defines a student by:
    attributes:
        first_name
        last_name
        age
Instantiation with first_name, last_name and age
public method to_json: that retrieves a dictionary representaion
of student instance
"""


class Student:
    """studen class"""
    def __init__(self, first_name, last_name, age):
        """Student inits"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of a
        student instance"""
        return self.__dict__
