#!/usr/bin/env python3

"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Week 5 Lab File Data Interactions
"""

hFile = open("/etc/passwd","r")
strfiletxt = hFile.read()
print(strfiletxt)
print(type(strfiletxt))
print(len(strfiletxt))
print("Len equals the length of the string")
print("You may want to use this tecnique to view all the contents in your file")
hFile.close()

hFile = open("/etc/passwd","r")
listfiletxt = hFile.readlines()
print(listfiletxt)
print(type(listfiletxt))
print(len(listfiletxt))
print("Len is counting the number of objects in the list in your file")
print("Use this technique to more clearly see the items listed in your file")
hFile.close()

hFile = open("/etc/passwd","r")
lines = 0
words = 0
characters = 0
for line in hFile:
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    characters = characters + len(line)
print(lines)
print(words)
print(characters)
print("Use this statement to find out how many lines/words/characters in file") 
hFile.close()



    






