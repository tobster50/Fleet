from Fleet import *
from Base import *
from ArmyAccount import *

class Army:
    def __init__(self, armyName):
        self.armyName = armyName
        self.armyID = 0
        self.armyDict = {}

    def armyInterface(self, armyID):
        user = self.armyDict[armyID]
        session = 0
        while session == 0:
            print("\nWelcome back Commander! What would you like to do today?")
            print("\n1: Build Structure")
            print("2: Create Units")
            print("3. Stats")
            choice = input("\nMake your choice: ")
            choice = int(choice)
            if choice == 1: #basic structure shop
                #base = Base.baseDict[armyID]
                Base.purchaseStructure(armyID)
            elif choice == 2:
                pass
            elif choice == 3: #show stats
                self.armyStats()
            else:
                print("Invalid input")

    def armyAccess(self):
        armyIdInput = input("\nInput your ID number: ")
        armyIdInput = int(armyIdInput)
        passwordInput = input("Input your password: ")
        check = self.passwordCheck(armyIdInput, passwordInput)
        if check == 1:
            self.armyInterface(armyIdInput)
    
    def generateArmy(self, armyName, armyPassword):
        armyID = self.armyID     
        newArmy = ArmyAccount(armyName, armyPassword, armyID)
        newBase = Base(armyID)
        self.armyDict[armyID] = newArmy
        newBase.baseDict[armyID] = newBase
        self.armyID = self.armyID + 1

    def createArmy(self):
        armyName = input("What is the name of your army? ")
        setPassword = 1
        while setPassword == 1:
            accountPassword = input("Set your password: ")
            passwordCheck = input("Re-enter your password: ")
            if accountPassword == passwordCheck:
                print("Password match")
                setPassword = 0
            else:
                print("Passwords do not match. Try again")
        self.generateArmy(armyName, accountPassword)
        
    def passwordCheck (self, accountNumber, accountPassword):
        user = self.armyDict[accountNumber]
        if accountPassword == user.armyAccountPassword:
            print("Password Match")
            return 1
        else:
            print("Password doesn't match")


    def armyStats(self):
        print(f"\nArmy Name: {self.armyName}")
        print(f"Total Structures: {self.armyStructures}")
        print(f"Army Power Supply: {self.armyPower}")
        print(f"Total Funds: ${self.armyFunds}")
        print(f"Income ${self.armyIncome} per hour")
        print(f"Total Units: {self.armyTotalUnits}")
        print(f"Available Units: {self.armyAvailableUnits}")
        print(f"Total Fleets: {self.armyFleets}")

        
        print(f"\nArmy Name: {armyName}")
        print(f"Army ID: {armyID}")
        print(f"Funds: {newArmy.armyAccountFunds}")
        print(f"Income: {newArmy.armyAccountIncome}")
        print(f"Total Units: {newArmy.armyAccountTotalUnits}")
        print(f"Available Units: {newArmy.armyAccountAvailableUnits}")
        print(f"Fleets: {newArmy.armyAccountFleets}")
        print(f"Base ID: {newBase.baseID}")
        print(f"Structures: {newBase.baseStructures}")
        print(f"Power: {newBase.basePower}")
        print(f"Research Level: {newBase.baseResearchLevel}")
        print(f"Unit Level: {newBase.baseUnitLevel}")