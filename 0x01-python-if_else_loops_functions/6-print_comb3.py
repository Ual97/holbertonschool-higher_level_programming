#!/usr/bin/python3
for j in range(0, 9):
    for i in range(j, 10):
        if j != 8:
            if j == 0:
                print("{:02d}, ".format(i), end="")
            elif j != 8:
                print("{:d}{:d}, ".format(j, i), end="")
print("89")
