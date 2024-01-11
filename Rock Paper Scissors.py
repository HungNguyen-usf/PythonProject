import random

CHOICES = ["rock", "paper", "scissors"]

def get_user_choice():
  user_choice = input("Type rock, paper, or scissors: ")
  while user_choice not in CHOICES:
    print("Invalid choice. Please type rock, paper, or scissors.")
    user_choice = input("Type rock, paper, or scissors: ")
  return user_choice

def get_computer_choice():
  return random.choice(CHOICES)

def play_game():
  user_choice = get_user_choice()
  computer_choice = get_computer_choice()
  print(f"\nYou threw '{user_choice}', the computer threw '{computer_choice}'")

if __name__ == "__main__":
  play_game()