#!/usr/bin/env python3

"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Celsius to Fahrenheit Conversion script
"""

def convert_celsius_to_fahrenheit(number):
    intnumber = int(number)
    convert = ((intnumber*9/5) + 32)
    return convert

def main():
    number = input("Please enter Celsius temperature:")
    number = convert_celsius_to_fahrenheit(number)
    print("Your temperature in Fahrenheit:", str(number))

if __name__ == "__main__":
    main()

 
