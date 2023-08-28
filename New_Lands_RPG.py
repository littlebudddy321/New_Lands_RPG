#import python libraries
import time, random, secrets, pickle, os, math


NAMES = ("Granek", "sarkol", "gestava", "sopane", "kela",
         "akabna", "woakna", "heyla", "hoesia", "Talklam",
         "sayanag", "guestavo", "leaknog", "Godta", "gem",
         "kakrela", "soyboi", "canfud", "saja", "loposa",
         "jeanna")

NAMESRAND = random.choice(NAMES)


#first starting area
Wood = random.randint(0, 10)
Stone = random.randint(0, 10)
Iron = random.randint(0, 10)
Gold = random.randint(0, 1)
Copper = random.randint(0, 10)
Fish = random.randint(0, 10)

#inventory
IWOOD = 0
ISTONE = 0
IIRON = 0
IGOLD = 0
ICOPPER = 0
IFISH = 0

#Xp system
Xp = 0
Level = 1
XpLEFT = 100



while True:
    print("Type 'help' for help.")
    print("========================================")
    Choose_action = input("choose action: ")

    match Choose_action: #Choose your action

        case "scan": #scan area for resources
            print("========================================")
            print("Resource list:")
            print("----------------------------------------")
            print("Wood", Wood, "\nStone", Stone, "\nIron",
                  Iron, "\nGold", Gold, "\nCopper", Copper,
                  "\nFish", Fish,)

        case "mine": #select collection mode
            while True:
                mine = input("choose resource: ")
                match mine:
                    case "wood":
                        if Wood >= 1:
                            print("you collected +1 wood")
                            Wood -= 1
                            IWOOD += 1
                            Xp += 10
                            XpLEFT -= 10
                        else:
                            print("there is no more resource to collect")

                    case "stone":
                        if Stone >= 1:
                            print("you collected +1 stone")
                            Stone-= 1
                            ISTONE += 1
                            Xp += 10
                            XpLEFT -= 10
                        else:
                            print("there is no more resource to collect")


                    case "iron":
                        if Iron >= 1:
                            print("you collected +1 iron")
                            Iron -= 1
                            IIRON += 1
                            Xp += 10
                            XpLEFT -= 10
                        else:
                            print("there is no more resource to collect")

                    case "gold":
                        if Gold >= 1:
                            print("you colleted +1 gold")
                            Gold -= 1
                            IGOLD += 1
                            Xp += 10
                            XpLEFT -= 10
                        else:
                            print("there is no more resource to collect")
                            
                    case "copper":
                        if Copper >= 1:
                            print("you collected +1 copper")
                            Copper -= 1
                            ICOPPER += 1
                            Xp += 10
                            XpLEFT -= 10
                        else:
                            print("there is no more resource to collect")

                    case "fish":
                        if Fish >= 1:
                            print("you collected +1 Fish")
                            Fish -= 1
                            IFISH += 1
                            Xp += 10
                            XpLEFT -= 10
                        else:
                            print("there is no more resource to collect")
        
                    case "stop":
                        break



    #xp system and leveling up calculations
    if Level >= 80:
        if XpLEFT <= 1:
            Level += 1
            XpCALC = Level * 1000
            XpLEFT += XpCALC    
    else:
        if Level >= 49:
            if XpLEFT >= 1:
                Level += 1
                XpCALC = Level * 500
                XpLEFT += XpCALC
        else:
            if Level >= 0:
                if XpLEFT <= 1:
                    Level += 1
                    XpCALC = Level * 100 + 100
                    XpLEFT += XpCALC
        


    match Choose_action: #continuation of choose you action
        case "bag": #check inventory
            print("========================================")
            print("Inventory:")
            print("----------------------------------------")
            print("Wood", IWOOD, "\nStone", ISTONE, "\nIron", IIRON, "\nGold", IGOLD, "\nCopper", ICOPPER, "\nFish", IFISH)

        case "help": #prints list of available commands
            print("scan, travel, mine, bag")

        case "level": #check level
            print("Total Xp earned", Xp)
            print("current level", Level)
            print("needed Xp to next level:", XpLEFT )

        case "travel": # travel to different section

            AttackChance = random.randint(0, 100)
            if AttackChance <= 50:
                ENEMYHEALTH = random.randint(15, 20)
                print("========================================")
                print("you have entered combat with a Saron bandit")
                print("----------------------------------------")
                print("Health:", ENEMYHEALTH)
                print("Name:", NAMESRAND)
                print("----------------------------------------")
                print("")
            while True:
                print("Type 'help' for help.")
                print("----------------------------------------")
                CHOOSE_ATTACK = input("Choose attack style: ")
                match CHOOSE_ATTACK:
                    case "slash":
                        print("")
                    case "block":
                        print("")
                    case "stab":
                        print("")
                    case "lunge":
                        print("")
                    case "run":
                        print("you run!")
                        break


            else:
                print("15 seconds until you arive at new area")
                print("========================================")
                time.sleep(1)
                print("you travel to the next sector")
                print("----------------------------------------")
                Wood = random.randint(0, 10)
                Stone = random.randint(0, 10)
                Iron = random.randint(0, 10)
                Gold = random.randint(0, 1)
                Copper = random.randint(0, 10)
                Fish = random.randint(0, 10)
