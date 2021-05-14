#!/usr/bin/env python3
"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Week 12 file transfer server script
"""

import socket

LHOST = ''
LPORT = 50008

L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while(1):
    L_SOCK.listen(1)
    L_CONN, addr = L_SOCK.accept()
    print('Connected by', addr)
    while 1:
        RCV_DATA = L_CONN.recv(1024)
        if not RCV_DATA: break
        f = open("week12dataoutput.txt", "a+")
        f.write("\nNew Line")


    L_CONN.close()

