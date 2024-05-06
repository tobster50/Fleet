import sys
from ArmyAccount import *
from Army import *

account = Army("admin")

login = 0 
while login == 0:
    print("\nWelcome to the war front commander!")
    print("1. Log in")
    print("2. Create New Army")
    choice = input("Select your Option (1-2) ")
    choice = int(choice)
    if choice == 1:
        account.armyAccess()
    elif choice == 2:
        account.createArmy()
    elif choice == 3:
        sys.exit()
 
