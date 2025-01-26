# Used for random number generating for order (CSV not used yet, will be later)
import random, csv

# list of names
names = ["name1", "name2", "name3", "name4", "name5", "name6"]

# Variable creation
repeatsFound = 0

# Loop enables the program to run again if any duplicates are found
while True:

    # Sets to 0, in case it's another value from previous iteration(s)
    repeatsFound = 0

    # Creates two randomised versions of the original lists
    names1 = random.sample(names, len(names))
    names2 = random.sample(names, len(names))

    # Prints out the lists
    print(names1)
    print(names2)

    # Checks each position in the 'names1' list, against that position in the 'names2' list
    for i in range(len(names)):

        # If a repeat is found, tell the user, and add 1 to the counter
        if names1[i] == names2[i]:
            print("Repeat found")
            repeatsFound += 1
            continue
        # If nothing found, do nothing (probably doesn't have to be here, will likely remove later)
        elif names1[i] != names2[i]:
            continue

    # If the program found repeats, tell the user, and the loop will start again
    if repeatsFound > 0:
        print("Lists have duplicate data")
        continue
    # If no repeats were found, tell the user and end the program
    elif repeatsFound == 0:
        print("No repeat data")
        exit()