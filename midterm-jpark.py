#!/usr/bin/env python3

"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Midterm Jurassic Park script
"""

print("Name: Andrew Krubsack")

password_database = {}
password_database = {"Username":"dnedry","Password":"please"}

command_database = {}
command_database = {"reboot":"OK. I will reboot all park systems."}
command_database["shutdown"] = "OK. I will shut down all park systems."
command_database["done"] = "I hate all this hacker stuff."

white_rabbit_object = 0
counter = 0

while white_rabbit_object == 0 and counter < 3:
    counter += 1
    print("Username:")
    input_user = input("->")
    print("Password:")
    input_password = input("->")
    

    # == UserName and Password Logic ======

    if (input_user == password_database["Username"]) and \
       (input_password == password_database["Password"]):
        white_rabbit_object = 1
        print("Hi, Dennis. You're still the best hacker in Jurassic Park.")
        print("Enter a command")

        print("1. reboot")
        print("2. shutdown")
        print("3. done")

        # == Command Logic ============
        command = input("->")

        if command in command_database.keys():
            print(command_database[command])
        
        else:
            print("The Lysine Contingency has been put into effect.")

    else:
        if counter < 3:
            print("You didn't say the magic word. {count}")
        
        else:
            repeat = "You didn't say the magic word.\n" * 25
            print(repeat)
        
