#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for k, v in new_dic.items():
        new_dic[k] = round(v * 2, 1)
    return (new_dic)
