print("Welcome to the tip calculator!") # Welcome message
bill = float(input("What was the total bill? $")) # Takes the input of the bill total. Input is converted to float and saved as a variable called "bill".
tip = int(input("What percentage tip would you like to give? 10, 12, 15, or another amount: ")) # Takes the input of the desired tip % total. Input is converted to an integer and saved as a variable called "tip".
tip += 100 #Adds 100 to the tip input for later calculations.
people = int(input("How many people to split the bill? ")) # Takes the input of the amount of people splitting the bill. Input is converted to an integer and saved as a variable called "people".
amount_per_person = bill/people # Calculates each persons amount owed before adding the tip.
tip_percent = tip/100 # Calculates the tip amount to use with calculation for final amount.
final_amount = round(amount_per_person*tip_percent, 2) # Calculates the final math, and rounds to 2 decimals.
print("Each person should pay:" + str(final_amount)) # Prints the results.
