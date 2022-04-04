#!/usr/bin/python3
"""
Function that writes a string and returns number of characters
written in UTF8 encoding
"""


def write_file(filename="", text=""):
    """writes a string and returns number of characters"""
    lines = 0
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
