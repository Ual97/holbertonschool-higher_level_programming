#!/usr/bin/python3
for cha in reversed(range(97, 123)):
    print("{:c}".format(cha if (cha % 2 == 0) else (cha - 32)), end='')
