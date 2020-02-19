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


# Main routine

# Ask user how much they want to play with (min $1, max $10)

balance = num_check("How much money would you like to play with? $", 1, 10)

keep_going = ""
while keep_going == "":

    # Tokens list includes 10 items to prevent too many unicorns being chosen
    tokens = ["horse","horse", "horse",
              "zebra", "zebra", "zebra",
              "donkey", "donkey", "donkey", "unicorn"]

    # Randomly choose a token from the list above
    token = random.choice(tokens)
    print()
    print("You got a {}".format(token))

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

# Farewell user at the end of the game.
print("Thank you for playing.")
