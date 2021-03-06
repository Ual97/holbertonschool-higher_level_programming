#!/usr/bin/python3
"""python scrpit that displays value of X-Request-Id from a url"""

from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
