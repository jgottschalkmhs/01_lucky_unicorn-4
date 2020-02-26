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



