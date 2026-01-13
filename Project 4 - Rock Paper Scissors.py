import random #Import the random module so the functions can be used.

#ASCII designs for rock, paper scissors
rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("Welcome to the Rock, Paper, Scissors Championship!\n" #Input for player choice. Enter 1, 2, 3
                      "Let's begin! Choose 0 for 'Rock', 1 for 'Paper', or 2 for 'Scissors'"))
options_pick = [rock, paper, scissors] #Creates a table to reference the ASCII images.

computer_choice = random.randint(0, 2) #Selects a random number between 0 and 2

print(f"You have chosen:\n {options_pick[player_choice]}")  #Prints message and ASCII depending on the players input. "f" makes it a f string so multiple types of data can be used on the same line without hassle.
                                                            # Don't forget to enclose in {}. [] are used to enclose player_choice because it's a list functon (technically an int, but they can function for list index's).
print(f"The computer has chosen:\n {options_pick[computer_choice]}")#Prints message and ASCII depending on the players input. "f" makes it a f string so multiple types of data can be used on the same line without hassle.
                                                            # Don't forget to enclose in {}. [] are used to enclose computer_choice because it's a list functon (technically an int, but they can function for list index's).
if player_choice == computer_choice: #self-explanatory
    print("It's a draw, play again")
elif    (player_choice == 0 and computer_choice == 2) or \
        (player_choice == 1 and computer_choice == 0) or \
        (player_choice == 2 and computer_choice == 1):  #lists all the possible win conditions under 1 statement.
                                                        # The parenthesis "()" groups the conditions so they are evaluated together.
                                                        # The backslash "\" allows the statement to be continued on the next line so the code looks clean.
    print("Congratulations you WIN!")
else:
    print("Sorry you LOSE!")
