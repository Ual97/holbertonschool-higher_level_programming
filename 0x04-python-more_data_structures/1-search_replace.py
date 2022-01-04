#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i in range(len(new)):
        if search == new[i]:
            new[i] = replace
    return (new)
