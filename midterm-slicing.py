#!/usr/bin/env python3

"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Midterm Slicing script
"""

print("Name: Andrew Krubsack")

hFile = open("slicing-file.txt","r")
listfiletxt = hFile.readlines()

"""
quote = " "
print("{listfiletxt[-3]}")
print(quote.join("{listfiletxt[2:5]}"))
print(quote.join("{listfiletxt[-10:-15:-2]}"))
print(quote.join("{listfiletxt[10:13]}"))
print(quote.join("{listfiletxt[-19:-22:-1]}".replace('\n','')))

"""

slice1 = listfiletxt[-3]
slice2 = " ".join(listfiletxt[2:5])
slice3 = " ".join(listfiletxt[-10:-15:-2])
slice4 = " ".join(listfiletxt[10:13])
slice5 = " ".join(listfiletxt[-19:-22:-1])

quote = slice1 + slice2 + slice3 + slice4 + slice5
quote = quote.replace("\n"," ")
print(quote)




