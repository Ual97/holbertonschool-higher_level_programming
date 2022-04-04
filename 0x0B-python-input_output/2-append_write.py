#!/usr/bin/python3
"""
function that appends a string to the end of a text file
in UTF8 enconding
"""


def append_write(filename="", text=""):
    """appends string to end of file"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
