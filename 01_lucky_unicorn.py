# Lucky unicorn decomposition step 2
# Generate a random token

import random

HOW_MUCH = 100
tokens = ["horse", "zebra", "donkey", "unicorn"]

uni_count = 0
zebhor_count = 0
donkey_count = 0

for item in range(0, HOW_MUCH):
    chosen = random.choice(tokens)

    if chosen == "unicorn":
        uni_count += 1
    elif chosen == "donkey":
        donkey_count += 1
    else:
        zebhor_count += 1
    print(chosen)

# Money calculations
winnings = uni_count * 5 + zebhor_count * 0.5

print("***Win / Loss Calculations***")
print("# Unicorns: {}".format(uni_count))
print("Donkeys: {}".format(donkey_count))
print("Zebras / horses: {}".format(zebhor_count))
print("You have won ${:.2f}".format(winnings))
