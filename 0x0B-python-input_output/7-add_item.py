#!/usr/bin/python3
"""
adds all arguments to a list (saved as JSON representation)
if the file does not exist, it must be created
"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

arg_list = sys.argv
new_list = (arg_list[1:])
try:
    current_content = load_from_json_file("add_item.json")
except FileNotFoundError:
    current_content = []
save_to_json_file(current_content + new_list, "add_item.json")
