#!/usr/bin/env python3

"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Midterm If Script
"""

print("Name:Andrew Krubsack")

hFile = open('Midterm-if.txt','r')


total = 0
keywordlist = ("gmeach18@ed.gov","248.253.63.149","Whiteland","80.222.19.190","Kayley","dcassyqw@microsoft.com")
for line  in hFile:
    for keyword in keywordlist:
        if keyword in line:
             total += int(line.split("," )[0]) 
             print(line)

print(total)   
hFile.close()
