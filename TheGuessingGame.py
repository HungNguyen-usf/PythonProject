import random


class rand_Num:
    def generate(self):
        global secret_number
        secret_number = random.randint(1, 10)
        return secret_number


guess_count = 0
guess_limit = 3
random_num = rand_Num()
random_num.generate()

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


