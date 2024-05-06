from Army import *
from ArmyAccount import *
class Base:
    def __init__ (self, baseID):
        self.baseID = baseID
        self.baseDict = {}
        self.baseStructures = 0
        self.basePower = 0
        self.baseResearchLevel = 1
        self.baseUnitLevel = 1

    def purchaseStructure(self, baseID):
        base = self.baseDict[baseID]
        if self.baseResearchLevel == 1:
            buildingStore = 0
            while buildingStore == 0:
                print("\nWhat would you like to purchase today? (1-5) (0 to quit)")
                print("1. Power Plant ($250)")
                print("2. Mining Plant ($500)")
                print("3. Hangar ($500)")
                print("4. Research Lab ($2000)")
                print(f"\n Current Balance ${base.armyAccountFunds}")
                purchase = input("Make your choice: ")
                purchase = int(purchase)
                if purchase == 0: #quit
                    buildingStore = 1
                elif purchase == 1: #power plant
                    if base.armyAccountFunds >= 250:
                        print("You purchased a Power Plant!")
                        print("$250 deducted from total funds!")
                        print("Power Supply increased by 500!")
                        base.armyAccountFunds = base.armyAccountFunds - 250
                        base.basePower = base.basePower + 500
                        base.baseStructures = base.baseStructures + 1
                    else:
                        print("Insufficent Funds!")
                elif purchase == 2: #mining plant
                    if base.armyAccountFunds >= 500:
                        print("You purchased a Mining Plant!")
                        print("$500 deducted from total funds!")
                        print("Income increased by 1000!")
                        base.armyAccountFunds = base.armyAccountFunds - 500
                        base.armyAccountIncome = base.armyAccountIncome + 1000
                        base.baseStructures = base.baseStructures + 1
                    else:
                        print("Insufficent Funds!")
                elif purchase == 3: # hangar
                    if base.armyAccountFunds >= 500:
                        print("You purchased a Hangar!")
                        print("$500 deducted from total funds!")
                        print("New vehicles now available for purchase!")
                        base.armyAccountFunds = base.armyAccountFunds - 500 
                        base.baseStructures = base.baseStructures + 1
                    else:
                        print("Insufficent Funds!")
                elif purchase == 4: #research lab
                    if base.armyAccountFunds >= 2000:
                        print("You purchased a Research Lab!")
                        print("$2000 deducted from total funds!")
                        print("Advanced buildings now available for purchase!")
                        base.armyAccountFunds = base.armyAccountFunds - 2000
                        base.baseResearchLevel = base.baseResearchLevel + 1
                        base.baseStructures = base.baseStructures + 1
                    else:
                        print("Insufficent Funds!")
                else:
                    print("Invalid input")

        elif self.armyTechLevel == 2:
                buildingStore = 0
                while buildingStore == 0:
                    print("\nWhat would you like to purchase today? (1-6) (0 to quit)")
                    print("1. Power Plant ($250)")
                    print("2. Mining Plant ($500)")
                    print("3. Hangar ($500)")
                    print("4. Advanced Power Plant ($500)")
                    print("5. Heavy Mining Plant ($1000)")
                    print("6. Mech Factory ($1500)")
                    print(f"\n Current Balance ${base.armyAccountFunds}")
                    purchase = input("Make your choice: ")
                    purchase = int(purchase)
                    if purchase == 0: #quit
                        buildingStore = 1
                    elif purchase == 1: #power plant
                        if base.armyAccountFunds >= 250:
                            print("You purchased a Power Plant!")
                            print("$250 deducted from total funds!")
                            print("Power Supply increased by 500!")
                            base.armyAccountFunds = base.armyAccountFunds - 250
                            base.basePower = base.basePower + 500
                            base.baseStructures = base.baseStructures + 1
                        else:
                            print("Insufficent Funds!")
                    elif purchase == 2: #mining plant
                        if base.armyAccountFunds >= 500:
                            print("You purchased a Mining Plant!")
                            print("$500 deducted from total funds!")
                            print("Income increased by 1000!")
                            base.armyAccountFunds = base.armyAccountFunds - 500
                            base.armyAccountIncome = base.armyAccountIncome + 1000
                            base.baseStructures = base.baseStructures + 1
                        else:
                            print("Insufficent Funds!")
                    elif purchase == 3: # hangar
                        if base.armyAccountFunds >= 500:
                            print("You purchased a Hangar!")
                            print("$500 deducted from total funds!")
                            print("New vehicles now available for purchase!")
                            base.armyAccountFunds = base.armyAccountFunds - 500 
                            base.baseStructures = base.baseStructures + 1
                        else:
                            print("Insufficent Funds!")
                    elif purchase == 4: #advanced power plant
                        if base.armyAccountFunds >= 500:
                            print("You purchased an Advanced Power Plant!")
                            print("$500 deducted from total funds!")
                            print("Power Supply Increased by 1000!")
                            base.armyAccountFunds = base.armyAccountFunds - 500
                            base.basePower = base.basePower + 1000
                            base.baseStructures = base.baseStructures + 1
                        else:
                            print("Insufficent Funds!")
                    elif purchase == 5: #heavy mining plant
                        if base.armyAccountFunds >= 500:
                            print("You purchased a Heavy Mining Plant!")
                            print("$1000 deducted from total funds!")
                            print("Income increased by 2000!")
                            base.armyAccountFunds = base.armyAccountFunds - 1000
                            base.armyAccountIncome = base.armyAccountIncome + 2000
                            base.baseStructures = base.baseStructures + 1
                        else:
                            print("Insufficent Funds!")
                    elif purchase == 6: #mech factory
                        if base.armyAccountFunds >= 1500:
                            print("You purchased a Mech Factory!")
                            print("$1500 deducted from total funds!")
                            print("New Units Available for purchase!")
                            base.armyAccountFunds = base.armyAccountFunds - 1500
                            base.baseStructures = base.baseStructures + 1
                        else:
                            print("Insufficent Funds!")
                else:
                    print("Invalid input")
