#!/usr/bin/python3
"""python scrpit that handles errors from requests"""

from sys import argv
from urllib import response
import urllib.request
import urllib.error

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
