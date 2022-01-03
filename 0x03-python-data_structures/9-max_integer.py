#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return (None)
    else:
        answer = None
        for i in my_list:
            if i > answer:
                answer = i
        return (answer)
