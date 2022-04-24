#!/usr/bin/python3
"""python scrpit that takes a letter and sends a POST request"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    payload = {'q': letter}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
