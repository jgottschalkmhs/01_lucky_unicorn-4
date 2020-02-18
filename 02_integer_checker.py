def num_check(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("please enter a number")


# Main routine
num_1 = num_check("Enter a number: ")
num_2 = num_check("Enter a second number: ")

num_3 = num_1 + num_2
# multiply two numbers together
num_4 = num_1 * num_2
# greet user and display math
print("The numbers that you have chosen add up to {}".format(num_3))
print("Your numbers also multiply to get {}".format(num_4))
