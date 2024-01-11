# Dice-Rolling-Simulator
import random


class DiceRollingSimulator:
    def __init__(self):
        self.num_sides = 6

    def roll_dice(self):
        return random.randint(1, self.num_sides)


def main():
    print("Welcome to the Dice Rolling Simulator!")
    simulator = DiceRollingSimulator()

    while True:
        user_input = input(" Please Press 'Enter' to roll the dice or 'q' to quit: ")

        if user_input.lower() == 'q':
            print("Thank you for using the Dice Rolling Simulator. Have a good day, Goodbye!")
            break

        roll_result = simulator.roll_dice()
        print(f"You rolled: {roll_result}")


if __name__ == "__main__":
    main()