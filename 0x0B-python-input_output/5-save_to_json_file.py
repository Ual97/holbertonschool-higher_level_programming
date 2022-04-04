#!/usr/bin/python3
"""
unction that writes an Object to a text file,
 using a JSON representation:
"""


def save_to_json_file(my_obj, filename):
    """write obj to text file using JSON"""
    import json
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
