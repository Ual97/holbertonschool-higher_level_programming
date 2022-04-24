#!/usr/bin/python3
"""python scrpit that displays value of X-Request-Id of a given url"""

from sys import argv
import urllib.request

reqs = urllib.request.Request(argv[1])
with urllib.request.urlopen(reqs) as response:
    print(response.headers['X-Request-Id'])
