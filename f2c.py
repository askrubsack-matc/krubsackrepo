#!/usr/bin/env python3

"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Week 9 script Functions
"""

def convert_fahrenheit_to_celsius(number):
    intnumber = int(number)
    #print(type(intnumber))
    convert = ((intnumber-32) * 5/9) 
    return convert

def main():
    number = input("Please enter Fahrenheit temperature:")
    number = convert_fahrenheit_to_celsius(number)
    print("Your temperature in Celsius:", str(number))

if __name__ == "__main__":
    main()







