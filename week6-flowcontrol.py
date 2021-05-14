#!/usr/bin/env python3

"""
Name: Andrew Krubsack
Email: askrubsack@madisoncollege.edu
Description: Week 6 Flow Control Script
"""

print("""You are standing in front of an abandoned looking castle with 3 doors.
Do you go through door #1, door #2, or door #3?""")

door = input("->")

# == Door Number 1 logic =========================
if door == "1":
	print("The front door is old and creaks. You see a suit of armor in the foyer.")
	print("What do you do?\n")

	print("1. Try the armor on.")
	print("2. Leave the armor be.")

	# == Armor logic =========================
	armor = input("->")
	if armor == "1":
		print("1) The armor fits like a charm! Yay new clothes!")
	elif armor == "2":
		print("2) No new clothes for you! Come back in 1 year and try again!")
	else:
		print(f"N)You did not see the {armor} perhaps you need an eye exam.")
		print("The optometrist is full till April.")

# == Door Number 2 Logic ==========================
elif door == "2":
	print("The trapdoor by the garden is locked tight. Do you try and open it?\n")

	print("1. Yes with the nearby garden rake.")
	print("2. Yes with the twig next to the tree.")
	print("3. Nope not a chance!")

	# == Trapdoor Logic ======================
	trapdoor = input("->")

	if trapdoor == "1" or trapdoor == "2":
		print("1) You cannot open a trapdoor without any quality tools!")
		print("1) Drat! Better luck next time!")
	else:
		print("N) Good choice not breaking and entering!")

# == Door Number 3 Logic =====================
elif door == "3":
        print("The hidden door under the drawbridge looks like a stone wall.")
        print("You are searching for a handle or button to open, where do you press?\n")

        print("1) The rock above your right eye.")
        print("2) The rock below your right foot.")
        print("3) The rock below your left foot.")
        
        # == Stone Logic =================
        stone = input("->")

        if stone =="1":
                print("1) Great work the stones release and the door opens!")
        else:
                print("N) You are getting a headache and want to go home, bummer!")


else:
	print("You chose not to go adventuring at the castle and to get ice cream instead!")


