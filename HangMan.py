import time

# welcome user
name = input("Welcome! What is your name? ")
print("Hello, " + name + ". Let's play hangman!")

# wait for 1 second
time.sleep(1)

print("Start guess...")
time.sleep(0.5)

# select the word to play with.
word = "florida"

# create variable with empty value
guesses = ''

# number of turns
turns = 10

# create a while loop
# check turns more than zero
while turns > 0:
    # make counter that starts with zero
    failed = 0

    # for every character in the word
    for char in word:
        # see if the character is in the player's guess
        if char in guesses:
            # print the character
            print(char, end="")
        else:
            # if not found, print a dash
            print("_", end="")
            # increase failed counter with one
            failed += 1

    # if failed is equal to zero
    if failed == 0:
        print("\nYou won")
        break

    # ask the user to guess a character
    guess = input("\nGuess a character: ")

    # set the player's guess to guesses
    guesses += guess

    # if the guess is not found in the word
    if guess not in word:
        # turns counter decrease by 1 (now 9)
        turns -= 1
        # print wrong
        print("Wrong")
        # how many turns are left
        print("You have", turns, "more guesses")

        # if the turns are equal to zero
        if turns == 0:
            # print "You lose"
            print("You lose")