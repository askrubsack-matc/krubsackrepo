#!/usr/bin/env python3

"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Temp conversion script both f2c and c2f
"""

import f2c,c2f


def convert_temp(measure=None, number=None):

    if measure == "fahrenheit":
        f2c.convert_fahrenheit_to_celsius(number)
        print(f2c.convert_fahrenheit_to_celsius(number))
        print("is your temperature in celsius")

    elif measure == "celsius":
        c2f.convert_celsius_to_fahrenheit(number)
        print(c2f.convert_celsius_to_fahrenheit(number))
        print("is your temperature in fahrenheit")

    else:
        print("Need to choose fahrenheit or celsius!")

def main():
    measure = input("Select fahrenheit or celsius:")
    number = int(input("What is the temperature:"))
    convert_temp(measure, number)
    
if __name__=="__main__":
    main()



