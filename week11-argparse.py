#!/usr/bin/env python3

"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Script using Argparse
"""
import sys
import argparse

parser = argparse.ArgumentParser(description='This is <your name here> script')

parser.add_argument('-m', dest='BASIC', help='Enter some text')

parser.add_argument('-i', '--integer', dest='varInt', metavar='[an integer]', type=int, required=True, help='<required> Enter a simple Integer')

parser.add_argument('-d', '--float', dest='varFloat', metavar='[a float]', type=float, help='Enter a simple float')

parser.add_argument('-s', '--string', dest='varString', metavar='[a string]', type=str, help='Enter a simple string')

parser.add_argument('-l', dest='varList', metavar='[strings]', default=[], nargs='+', required=False, help='Enter a list of strings (space delimited)')

parser.add_argument('-t', '--set-true', dest='bool_t', default=False, action='store_true', required=False, help='Toggle from default False to True')

parser.add_argument('-f', '--setfalse', dest='bool_f', default=True, action='store_false', required=False, help='Toggle from default True to False')

parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()

print(type(parser.parse_args().varBasic))
print(type(parser.parse_args().varInt))
print(type(parser.parse_args().varFloat))
print(type(parser.parse_args().varString))
print(type(parser.parse_args().varList))
