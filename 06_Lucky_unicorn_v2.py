# Number checking function
# Program should work - needs to be tested for usability

import random

# Integer checking function below


def num_check(question, low, high):
    valid = False
    while not valid:
        error = "Please enter a number between {} and {}".format(low, high)
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)


def token_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()
# Main routine

# Cost payout constants
COST = 1        # cost per round
UNICORN = 5     # unicorn wins $5
ZEB_HOR = 0.5   # zebra / horse 'wins' 50c
DONKEY = 0      # donkey does not win anything

# Introduction / Instructions

print("**** Welcome to the Lucky Unicorn Game ****")
print()
print("To play, enter an amount of money between $1 and $10 (whole dollars only).")
print()
print("- It costs $1/round")
print()
print("Payouts...")
print("-Unicorn: ${:.2f}".format(UNICORN))
print("-Horse / Zebra: ${:.2f}".format(ZEB_HOR))
print("-Donkey: ${:.2f}".format(DONKEY))
print()

# Ask user how much they want to play with
balance = num_check("How much money would you like to play with? $", 1, 10)
round_count = 0

print("***** Game in Progress *****")

keep_going = ""
while keep_going == "":

    # Tokens list includes 10 items to prevent too many unicorns being chosen
    tokens = ["horse", "horse", "horse",
              "zebra", "zebra", "zebra",
              "donkey", "donkey", "donkey", "unicorn"]

    # Randomly choose a token from the list above
    token = random.choice(tokens)
    round_count += 1

    # Adjust balance based on the chosen token and generate feedback
    if token == "unicorn":
        balance += 5     # wins $5
        feedback = "Congratulations, you won $5.00"
    elif token == "donkey":
        balance -= 1     # does not win anything (ie: loses $1)
        feedback = "Sorry you did not win anything in this round"
    else:
        balance -= 0.5    # 'wins' 50c, paid $1 so loses 50c
        feedback = "Congratulations, you won 50c"
    print()

    print(feedback)
    print("You have ${:.2f} to play with.".format(balance))

    # If user has enough money to play, ask if they want to play again.
    if balance < 1:
        print("Sorry you don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit. ")
print()

# Farewell user at the end of the game.
print("You played {} rounds and leave with ${:.2f}".format(round_count, balance))
print("Thank you for playing.")
