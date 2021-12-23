#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        print("1 argument:")
        print("1: ", end='')
        print("{:s}".format(sys.argv[1]))
    elif len(sys.argv) > 2:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{:d}: ".format(i), end='')
            print("{:s}".format(sys.argv[i]))
    else:
        print("0 arguments.")
