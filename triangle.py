#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: November 2019
# This program calculates the area of a triangle


def calculate_area(length, width):
    # calculate area

    # process
    area = (length / 2) * width

    # output
    print("The area is {0} cm²".format(area))


def main():
    # this function gets length and width

    try:
        # input
        length_from_user = int(input("Enter the length of a triangle (cm): "))
        width_from_user = int(input("Enter the width of a triangle (cm): "))
        print("")

        # call functions
        calculate_area(length_from_user, width_from_user)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
