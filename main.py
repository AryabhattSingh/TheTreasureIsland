print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''', end="")

print("""       
                Welcome to The Treasure Island 🏝 ️.\n
                Your mission is to find the treasure 💰.
                You're at a cross road ➕.
                Where do you want to go?
                Type \"left\" ⬅ ️ or \"right\" ➡ ️""")

choice = input("\nEnter your choice : ").lower()

if choice == "left":
    choice = input("""
                You've come to a lake ☱.
                There is an island 🏝  ️in the middle of the lakee️ ☱."
                Type \"wait\" 🕛 to wait for a boat ⛵.
                Or Type \"swim\" 🏊🏾 to swim across lake ☱."
                \nEnter your choice : """).lower()
    if choice == "wait":
        choice = input("""
                You arrive at the island unharmed.
                There is a house 🏚️ with 3 doors 🚪 🚪 🚪. One \"red\"🔴,  one \"yellow\"🟡 and one \"blue\"🔵.
                Which colour do you choose?"
                \nEnter your choice : """).lower()
        if choice == "red":
            print("""
                Burned by fire 🔥. Game Over.""")
        elif choice == "blue":
            print("""
                Eaten by beasts 🦁. Game over.""")
        elif choice == "yellow":
            print("""
                You found the treasure 🗝 🧰  ️💰. YOU WIN!""")
        else:
            print("""
                You fell in a trap 🪤. Game Over".""")
    else:
        print("""
                Attacked by trout 👿. Game Over.""")
else:
    print("""
                Killed by a boobytrap 🏹. Game Over.""")
