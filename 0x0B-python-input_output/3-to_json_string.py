#!/usr/bin/python3
"""
function that retruns JSON rep. of an object(string)
"""


def to_json_string(my_obj):
    """JSON representation of a string"""
    import json
    return json.dumps(my_obj)
