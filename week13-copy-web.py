#!/usr/bin/env python3
"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Week 13 copy webpage script
"""

import requests

response = requests.get("https://notpurple.com")

with open("my_web_file.html", "w") as hFile:
    hFile.write(response.text)

