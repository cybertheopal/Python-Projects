print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total_price = 0
if size == "S":
    total_price += 15
    if pepperoni == "Y":
        total_price += 2
        if extra_cheese == "Y":
            total_price += 1
            print("Your total is $" + str(total_price))
        else:
            print("Your total is $" + str(total_price))
    elif extra_cheese == "Y":
        total_price += 1
        print("Your total is $" + str(total_price))
    else:
        print("Your total is $" + str(total_price))
elif size == "M":
    total_price += 20
    if pepperoni == "Y":
        total_price += 3
        if extra_cheese == "Y":
            total_price += 1
            print("Your total is $" + str(total_price))
        else:
            print("Your total is $" + str(total_price))
    elif extra_cheese == "Y":
        total_price += 1
        print("Your total is $" + str(total_price))
    else:
        print("Your total is $" + str(total_price))
else:
    total_price += 25
    if pepperoni == "Y":
        total_price += 3
        if extra_cheese == "Y":
            total_price += 1
            print("Your total is $" + str(total_price))
        else:
            print("Your total is $" + str(total_price))
    elif extra_cheese == "Y":
        total_price += 1
        print("Your total is $" + str(total_price))
    else:
        print("Your total is $" + str(total_price))
