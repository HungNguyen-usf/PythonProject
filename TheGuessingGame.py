import random

# Create a class which generate random number from 1-10
class rand_Num:
    def generate(self):
        global secret_number
        secret_number = random.randint(1, 10)
        return secret_number


# Set the guess count and guess limit as well as creating a new randomly generated number
guess_count = 0
guess_limit = 3
random_num = rand_Num()
random_num.generate()

# Using while loops for when the guess count is still in limit or when they guess the correct number
# within the guess limit
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess != secret_number:
        print("Incorrect number, try again!")
    if guess == secret_number:
        print("Congrats, you are correct!")
        break
    elif guess_count == guess_limit:
        print("Sorry, you failed")
        print(f"The correct number is: {secret_number}")


