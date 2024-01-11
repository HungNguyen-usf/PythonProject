# In blackjack the dealer gives you two cards and themselves two cards. The goal is to get two cards that add up to 21
# If you don't have 21 exactly, the closer you are to 21 the better. If you exceed 21, you bust and lose your bet.
# I attempted to include a betting function but it could barely work and wasn't saving winnings.
# If you want another card, you Hit and will recieve another card along with its value.
# The dealer will also always hit if their hand is less than 16.
# If you don't want to hit for another card and risk a bust, you can choose to Stand and the dealer will reveal their second card.
# If the dealer's hand worth is greater than yours, you lose and vice versa. If hands are equal in worth, its a tie or "push" and bets are normally returned
# There are a few other choices you have playing blackjack which are well outside of my capabilities, so the only options here and hit and stand until you win or loose.
import os


import random

deck = [" 2 of Clubs", " 3 of Clubs", " 4 of Clubs", " 5 of Clubs", " 6 of Clubs", " 7 of Clubs", " 8 of Clubs",
        " 9 of Clubs", " 10 of Clubs", " 10 King of Clubs", " 10 Queen of Clubs", " 10 Jack of Clubs",
        " 11 Ace of Clubs",
        " 2 of Hearts", " 3 of Hearts", " 4 of Hearts", " 5 of Hearts", " 6 of Hearts", " 7 of Hearts", " 8 of Hearts",
        " 9 of Hearts", " 10 of Hearts", " 10 King of Hearts", " 10 Queen of Hearts", " 10 Jack of Hearts",
        " 11 Ace of Hearts",
        " 2 of Diamonds", " 3 of Diamonds", " 4 of Diamonds", " 5 of Diamonds", " 6 of Diamonds", " 7 of Diamonds",
        " 8 of Diamonds", " 9 of Diamonds", " 10 of Diamonds", " 10 King of Diamonds", " 10 Queen of Diamonds",
        " 10 Jack of Diamonds", " 11 Ace of Diamonds",
        " 2 of Spades", " 3 of Spades", " 4 of Spades", " 5 of Spades", " 6 of Spades", " 7 of Spades", " 8 of Spades",
        " 9 of Spades", " 10 of Spades", " 10 King of Spades", " 10 Queen of Spades", " 10 Jack of Spades",
        " 11 Ace of Spades"]

# Dealer and player recieve two random cards
plist = (random.sample(deck, 2))
dlist = (random.sample(deck, 2))

print("Your hand:")
print(plist)


def hand_Worth():
    # Initialize blank strirngs
    pstr = ""
    dstr = ""

    # Combining the pair of strings from Dlist and Plist
    dstr = dstr.join(dlist)
    pstr = pstr.join(plist)

    # Extracting integers from Dlist and Plist
    phand = [int(i) for i in pstr.split() if i.isdigit()]
    dhand = [int(i) for i in dstr.split() if i.isdigit()]

    # Adding integer to determine hand worth
    global pval
    global dval
    pval = phand[0] + phand[1]
    dval = dhand[0] + dhand[1]

    print("Hand is currently worth", pval)
    print("Type Hit to receive another card, and Stand to reveal the dealers hand")
    if pval == 21:
        print("Black Jack!")
    return (dval)
    return (pval)


hand_Worth()

# Dealer has to pull from deck if the hand worth is less than or equal to 16
while dval <= 16:
    dlist_hit = (random.sample(deck, 1))
    dlist.extend(dlist_hit)

    dstr_hit = ""
    dstr_hit = dstr_hit.join(dlist_hit)

    dhit = [int(i) for i in dstr_hit.split() if i.isdigit()]

    dval = dval + dhit[0]
    if dval >= 17:
        break


# Player Stand outcomes
def stand():
    print("Dealer hand is worth", dval)
    print(dlist)
    if dval == pval:
        print("Push! Hands Are Equal")
        print("Dealer hand is worth", dval)
        print("Player hand is worth", pval)
    elif dval == 21:
        print("Black Jack! The Dealer has won!")
    elif dval < pval:
        print("You have beat the Dealer!")
    elif dval > pval and dval > 21:
        print("Dealer bust! You win!")
    elif dval > pval:
        print("The Dealer has won!")


# Player Hit outcomes
def hit():
    global pval
    plist_hit = (random.sample(deck, 1))

    pstr_hit = ""
    pstr_hit = pstr_hit.join(plist_hit)

    phit = [int(i) for i in pstr_hit.split() if i.isdigit()]

    print(pstr_hit)
    print(phit)
    pval = pval + phit[0]
    print(pval)
    print("Hand is currently worth", pval)
    if pval > 21:
        print("Bust!")

    elif pval == 21:
        print("Black Jack!")
    elif pval < 21:
        print("Hit again? Or stand?")
    playerinput = {'Hit': hit, 'Stand': stand}
    action = input()
    playerinput[action]()


playerinput = {'Hit': hit, 'Stand': stand}
action = input()
playerinput[action]()

import sys
import os
python = sys.executable
os.execl(python, python, * sys.argv)