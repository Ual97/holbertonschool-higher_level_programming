#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numpos = number * (-1)
if number < 0:
    if numpos % 10 == 0:
        print("Last digit of {:d} is\
 {:d} and is 0".format(number, numpos % 10))
    elif numpos % 10 > 5:
        print("Last digit of {:d} is\
 {:d} and is greater than 5".format(number, numpos % 10))
    elif numpos % 10 < 5:
        print("Last digit of {:d} is {:d} and\
 is less than 6 and not 0".format(number, numpos % 10))
elif number > 0:
    if number % 10 == 0:
        print("Last digit of {:d} is {:d}\
 and is 0".format(number, number % 10))
    elif number % 10 > 5:
        print("Last digit of {:d} is {:d} and\
 is greater than 5".format(number, number % 10))
    elif number % 10 < 5:
        print("Last digit of {:d} is {:d} and is\
 less than 6 and not 0".format(number, number % 10))
