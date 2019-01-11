# -*- coding: utf-8 -*-
# This is a small app that helps make decisions (and allows me to teach myself Python)
# Beware of actually following this app's advice!

print("I heard you had a tough decision to make? Maybe I can help.")

# Get the number of option
num_options = int(input("Enter the number of options you have: "))

# Declare a list of options
option = []

# Let's ask for the what the options are
# Remember to use range() to make an x that is iterable, and to use the append thing
for i in range(num_options):
    option.append(input("What is option number " + str(i+1) + ": "))

# Now we throw the die – remember to reduce the len() by 1 because random.randint includes the endpoints
import random
choice = random.randint(0,len(option)-1)

# Let's give some potentially really bad advice
print("We (irresponsibly) recommend going with option number " + str(choice+1) + ", which is " + str(option[choice]) + ".")