#!/usr/bin/python3

if _name_ == "_main_":
    """Print the addition of all arguments."""
    Import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
