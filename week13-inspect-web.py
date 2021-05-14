#!/usr/bin/env python3
"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Week 13 inspect web script
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://notpurple.com")
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

soup.find('title')
print (soup.find('title'))

for link in soup.find_all ('a'):
    print (link.get('href'))



