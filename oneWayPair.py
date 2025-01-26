# Used for random number generating for order (CSV not used yet, will be later)
import random, csv
import sys
import time as t

# list of names
names = ["name1", "name2", "name3", "name4", "name5", "name6"]

while True:
    repeatsFound = 0
    names1 = random.sample(names, len(names))
    names2 = random.sample(names, len(names))

    # Checks each position in the 'names1' list, against that position in the 'names2' list
    for i in range(len(names)):

        # If a repeat is found, tell the user, and add 1 to the counter
        if names1[i] == names2[i]:
            repeatsFound += 1
            continue

        # If nothing found, do nothing (probably doesn't have to be here, will likely remove later)
        elif names1[i] != names2[i]:
            continue

    # If the program found repeats, tell the user, and the loop will start again
    if repeatsFound > 0:
        continue

    # If no repeats were found, tell the user and end the program
    elif repeatsFound == 0:
        print(*names1)
        print(*names2)
        print("Success!")

        exitPrompt = input()
        if exitPrompt == "":
            exit()
        else:
            exit()