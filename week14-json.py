#!/usr/bin/env python3
"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Week 14 JSON script
"""

import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Creating a parser to add arguments')

parser.add_argument('-ip', '--string', dest='IPinfo', metavar='[a String]', type=str, required=True, help='<required> Enter an IP Address')

IP = parser.parse_args().IPinfo

json_raw = requests.get(f"http://ipinfo.io/{IP}/json")
myDict = json.loads(json_raw.text)


for key in myDict:
    print(f"{key} : {myDict[key]}")


    
