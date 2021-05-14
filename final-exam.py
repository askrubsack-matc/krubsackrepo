#!/usr/bin/env python3
"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Final Exam
"""

import argparse
import requests
from bs4 import BeautifulSoup
import json
import socket
remoteHost = '172.31.28.253'
remotePort = range(5000-6000)
myHeaders={"content-type" :"text"}

parser = argparse.ArgumentParser(description = "Creating a parser to add arguments")
parser.add_argument('-ip', '--string', dest='ipaddress', type=str, help='Enter an IPv4 address')
parser.add_argument('-f', '--integer', dest='function', type=int, help='Enter an integer 1,2,3,4 or 5')

ipaddress = parser.parse_args().ipaddress
function = parser.parse_args().function

URL =(f"http://{ipaddress}/q{function}")

if function == 1:
    get_response = requests.get("http://172.31.28.252/q1")
    print("Name: Andrew Krubsack")
    print(URL)
    print(f"ANSWER: {get_response.text}")

elif function == 2:
    parse_string = requests.get("http://172.31.28.252/q2")
    soup = BeautifulSoup(parse_string.text, 'html.parser')
    print("Name: Andrew Krubsack")
    print(URL)
    for heading in soup.find_all("h3"):
        print(f"ANSWER: {heading.text[2:42:3]}")

elif function == 3:
    parse_header = requests.get("http://172.31.28.252/q3", headers=myHeaders)
    print("Name: Andrew Krubsack")
    print(URL)
    print(f"ANSWER: {parse_header.headers['MATC-HEADER']}")

elif function == 4:
    parse_json = requests.get("http://172.31.28.252/q4")
    print("Name: Andrew Krubsack")
    print(URL)
    Music_And_Books = json.loads(parse_json.text)
    for key in Music_And_Books:
        print(f"ANSWER:{key} : {Music_And_Books[key]}")

elif function == 5:
    socket_client = requests.get("http://172.31.28.253/q5")
    print("Name: Andrew Krubsack")
    print(URL)
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSocket.connect((remoteHost,remotePort))
    clientSocket.send(b"Secret")
    receivedData = clientSocket.recv(1024)
    print(receivedData.decode())

else:
    print("oh bother")












