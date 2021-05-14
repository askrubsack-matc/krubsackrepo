#!/usr/bin/env python3

"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Week 4 Lab DataTypes and Sequences
"""

varString = "Here is a nice string to slice"
varTuple = ("Here","is","a","nice","tuple","to","slice")
varList = ["Here","is","a","nice","list","to","slice"]

print(f"{varString[3:]}")
print(f"{varString[:3:]}")
print(f"{varString[3:12:]}")
print(f"{varString[::2]}")
print(f"{varString[::-1]}")
print(f"{varList[::-1]}")
print(f"{varList[2::-1]}")
print(f"{varList[2:4]}")
print(f"{varList[::3]}")
print(f"{varList[1:]}")
for element in varString:
        print(element)

for element in varList:
        print(element)

        






















