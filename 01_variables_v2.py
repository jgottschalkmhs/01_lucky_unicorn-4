# Number checking function


def num_check(question, low, high):
    valid = False
    while not valid:
        error = "Please enter a number between {} and {}".format(low, high)
        try:
            response = int(input("Enter a number between {} and {}: ".format(low, high)))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)


# Main routine
num_1 = num_check("Enter a number between 1 and 10: ", 1, 10)
num_2 = num_check("Enter a second number between one and ten: ", 1, 10)

num_3 = num_1 + num_2
# multiply two numbers together
num_4 = num_1 * num_2
# greet user and display math
print("The numbers that you have chosen add up to {}".format(num_3))
print("Your numbers also multiply to get {}".format(num_4))
