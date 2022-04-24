#!/usr/bin/python3
"""python scrpit that displays value of X-Request-Id of a given url"""

from sys import argv
import urllib.request

req = urllib.request.Request(argv[1])
with urllib.request.urlopen(req) as response:
    print(response.headers['X-Request-Id'])
