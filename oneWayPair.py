# Used for random number generating for order (CSV not used yet, will be later)
import random, csv

# list of names
f = open("names.csv", "r")

# reading the file
data = f.read()

# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
names = data.split("\n")


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

        # for each position in both of the list, print both names
        for valA, valB in zip(names1, names2):

            # Opens in write mode to wipe the file from previous uses (if any) and closes the file
            open("results.csv", "w").close()

            # Opens the file, using append, setting newline to blank ('') to stop empty rows
            with open("results.csv", "a", newline='') as f:
                writer = csv.writer(f)

                # Cell 1 has the first name, cell 2 has an arrow, cell 3 has the second name
                writer.writerow([valA,'->', valB])

            print(valA, "->", valB)

        # Just here so the user knows it's done, and for my satisfaction
        print("Success!")

        # A simple way to make any key exit the program
        exitPrompt = input("Press enter to exit")
        if exitPrompt == "":
            exit()
        else:
            exit()