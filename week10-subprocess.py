#!/usr/bin/env python3

"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Week 10 Subprocess script
"""

import subprocess

myProc = subprocess.run(['ps','-axco','command'], stdout=subprocess.PIPE)
output = myProc.stdout.decode().split('\n')

myProcString = output
#myProcList = [myProcString]
#print(len(myProcList))

for process in myProcString:
    print(process,'\n')








