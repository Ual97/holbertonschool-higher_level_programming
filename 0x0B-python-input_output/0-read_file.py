#!/usr/bin/python3
"""
Function That reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """reads file and prints to stdout"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
