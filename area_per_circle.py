#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: September 21, 2022
# This program calculates the area and circumference of a circle
# with a radius of 15mm.


# Imports
import math


def main():
    print("For a circle with the radius 15mm: \n")
    print("The area is: {} mm^2".format(math.pi * 15**2))
    print("The circumference is: {} mm".format(2 * math.pi * 15))


if __name__ == "__main__":
    main()
