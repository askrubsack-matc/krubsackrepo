#!/usr/bin/env python3

"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Week 7 Dictionaries
"""

myDictionary = {"server1.testlab.com":"192.168.1.10"}
myDictionary["server2.testlab.com"] = "192.168.1.11"
myDictionary["server3.testlab.com"] = "192.168.1.12"
myDictionary["server4.testlab.com"] = "192.168.1.13"
myDictionary["server5.testlab.com"] = "192.168.1.14"
myDictionary["server6.testlab.com"] = "192.168.1.15"
myDictionary["server7.testlab.com"] = "192.168.1.16"
myDictionary["server8.testlab.com"] = "192.168.1.17"

print(myDictionary)

print("My FQDN's are: ", myDictionary.keys())
print("My IP Addresses are:", myDictionary.values())
print("My FQDN's and IP Addresses are:",myDictionary.items())

# Which FQDN's are in myDictionary
# =================================

while True:
    found = False
    search = input("Which FQDN are you looking for?: ")

    if search == "DONE":
        print("The search has concluded")

        break
    for FQDN in myDictionary:
        if FQDN == search:
            found = True
            print(f"You have found your FQDN {search}")
            print(f" FQDN : {myDictionary[FQDN]}")
    if not found:
        print("Did not find your FQDN")



