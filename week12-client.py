#!/usr/bin/env python3
"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Week 12 Sockets client script
"""

import socket

RHOST = '127.0.0.1'
RPORT = 50006
SND_DATA = 'Sending multiple messages'

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

C_SOCK.send(bytearray(SND_DATA, 'utf8'))

RCV_DATA = C_SOCK.recv(1024)

print(RCV_DATA)

C_SOCK.close()


