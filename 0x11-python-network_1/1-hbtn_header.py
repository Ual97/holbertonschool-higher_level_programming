#!/usr/bin/python3
"""python scrpit that displays value of X-Request-Id of a given url"""

from sys import argv
import urllib.request

with urllib.request.urlopen(argv[1]) as response:
    html = response.read()
    print(response.headers['X-Request-Id'])
