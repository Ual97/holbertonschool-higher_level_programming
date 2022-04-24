#!/usr/bin/python3
"""python scrpit that sends POST request to given url"""

from sys import argv
import requests


if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
