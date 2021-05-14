#!/usr/bin/env python3
"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Week 12 file transfer client script
"""

import socket

RHOST = '127.0.0.1'
RPORT = 50008

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

hFile=open("week12data.txt", "r")
SND_DATA = hFile.read()

C_SOCK.send(bytearray(SND_DATA, 'utf8'))

C_SOCK.close()


