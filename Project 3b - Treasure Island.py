print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction_pick = input("After getting off your boat on Treasure Island, you enter a forest.\n" # Takes the users input and stores it in the variable direction_pick.
                       "There is a fork in the road with the option to go left or right.\n"
                       "Which direction do you choose? ")
if direction_pick != "left" and direction_pick != "Left": # If statement that triggers if the users input is anything other than "left" and "Left".
    print("You followed the path and got lost in the forest. While wondering, you fall into a whole and die a HORRIBLE and LONELY DEATH")
else:
    lake_pick = input("After walking for hours you approach a lake.\n" # Else statement that takes the users input and stores it in the variable lake_pick.
                  "You see a sign saying there is a local river-man who can take you across, however it does not say when he will appear.\n"
                  "You are an extremely strong swimmer and can swim across very easily.\n"
                  "Do you wait or do you swim? ")
    if lake_pick != "wait" and lake_pick != "Wait": # If statement that triggers if the users input is anything other than "wait" and "Wait".
        print("You jump into the water and start swimming across. You reach halfway and everything is going smoothly.\n"
              "Suddenly you feel something brush on your leg. You quickly flinch and start treading and looking around.\n"
              "Before you can start swimming again something GRABS your leg! You are dragged under water and are never heard from again.")
    else:
        door_pick = input("Your patience pays off. After roughly 45 minutes you see an old man in tribal attire rowing towards the sign.\n" # Else statement that takes the user input and stores it in the variable door_pick.
                  "He takes you to the other side of the river and tells you up ahead there is a house that was built by a man who had untold treasures with him when he was alive.\n"
                  "You walk through the forest and like the river-man said there is a house. You walk up and find the door is unlocked.\n"
                  "You open it and peak in. Inside the house there is nothing but 3 doors. A Red one, a Yellow one, and a Blue one.\n"
                  "You believe the treasure is behind one of these doors.\n"
                  "Which door to you choose to enter? ")
        if door_pick == "Red" or door_pick == "red": # If statement that triggers if the user inputs "red" or "Red".
            print("You open the door and walk in. The door locks behind you.\n"
                  "You start to look around, but notice it is suddenly get warmer. Out of no-where the room the room spontaneously explodes.\n"
                  "You get cooked like BBQ chicken.")
        elif door_pick =="Blue" or door_pick == "blue": # If statement that triggers if the user inputs "blue" or "Blue".
            print("You open the door and walk in. The door locks behind you.\n"
                  "You start to look around. and see a long pathway that is engulfed in darkness.\n"
                  "You hear a low growling sound coming from down the hallway. You, can't see anything but you feel like 'something'... can see you.\n"
                  "You start taking steps backwards, heading back to the door. But you hear the sound of something running at you.\n"
                  "Before you can make it too the door a wild BIGFOOT attacks you and eats you. You were delicious")
        elif door_pick == "Yellow" or door_pick == "yellow": # If statement that triggers if the user inputs "yellow" or "Yellow".
            print("You open the door and walk in. The door locks behind you.\n"
                  "You see another closed door ahead of you. You can see light shining from the frame of the door.\n"
                  "You slowly walk up and open the door cautiously. Behind the door you find a impossibly huge room filled so much treasure you can swim in it like Scrooge McDuck!\n"
                  "CONGRATULATIONS! You have found the treasure and have become rich beyond your wildest dreams. Enjoy your life!\n"
                  "Just don't dive in head first, you WILL die. The movies lied.")
        else:
            print("You must select Red, Yellow, or Blue") # If statement that triggers if anything other than the colours listed above are given as input.
