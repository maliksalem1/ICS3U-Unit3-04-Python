#!/usr/bin/env python3

# Created by: maliksalem1
# Created on: Oct 2022
# This program checks if a number is positive or negative

import constants


def main():
    # This function sees if your number is positive or negative

    # Input
    integer = int(input("Enter an integer: "))
    print("")

    # Process and Output
    if integer > constants.ZERO:
        print("{0} is a positive number.".format(integer))
    elif integer < constants.ZERO:
        print("{0} is a negative number.".format(integer))
    else:
        print("Your number is zero.")

    print("\nDone.")


if __name__ == "__main__":
    main()
