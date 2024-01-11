"""
This is a the final project for LIS 4930.
The goal of this project is to show that I am able to utilize different aspects of what I have
learned in this class in order to solve a problem.

In this project I will be creating a system of dice rolls based off of Dungeons and Dragons where the user will select what type of weapon is used, and then the characteristics of the weapon will be utilized in order to determine 1) To Hit, 2) Damage done. The user will also have the ability to 'roll stats' for their character (this will include all 6 base stats for a character, as well as using those stats to determine the other derived stats such as health and initiative), where each stat will determine different bonuses. The user will then be able to pick an enemy to fight, and will play a turn based game where after each action current stats are presented for both the user and the enemy.
"""

import random

"damage types 1= bludgeoning, 2= piercing, 3= slashing, 4= magic"


def weapon_select(x):
    weap = {}
    if x == 1:
        print("You have selected to use: Magic")
        weap = {
            "damage": 4,
            "d_t": 4
        }
    elif x == 2:
        print("You have selected to use: Dagger")
        weap = {
            "damage": 4,
            "d_t": 2
        }
    elif x == 3:
        print("You have selected to use: Shortsword")
        weap = {
            "damage": 6,
            "d_t": 3
        }
    elif x == 4:
        print("You have selected to use: Warhammer")
        weap = {
            "damage": 8,
            "d_t": 1
        }
    elif x == 5:
        print("You have selected to use: Pike")
        weap = {
            "damage": 10,
            "d_t": 2
        }
    else:
        print("You have selected to use: Greataxe")
        weap = {
            "damage": 12,
            "d_t": 3
        }
    return weap


def mon_select(x):
    monster = {}
    if x == 1:
        monster = {
            "name": "Easy",
            "hp": 10,
            "armor": 10,
            "damage": 4,
            "d_v": [1, 2, 3],
            "d_r": [0]
        }
    elif x == 2:
        monster = {
            "name": "Medium",
            "hp": 20,
            "armor": 14,
            "damage": 8,
            "d_v": [4],
            "d_r": [1, 2]
        }
    else:
        monster = {
            "name": "Hard",
            "hp": 30,
            "armor": 18,
            "damage": 12,
            "d_v": [1],
            "d_r": [2, 3]
        }
    return monster


"This is the introduction to the game"

print(
    "Welcome to DnD Lite, in this program, you will be creating a character by choosing stat distribution, weapons to use, and selecting a monster to fight to test your newly created character. Good Luck, and Have Fun.\n\n")

"This section of code allows the user to choose stat priority, and rolls stats, then creates modifiers based off of those stats that will be used in combat."

print(
    "You now get the choice of stat importance between: \n\n1) Strength: Determines the modifier for your chance to hit and bonus damage dealt with melee weapons.\n\n2) Intelligence: Determines the modifier for damage with magic (magic will always hit, but does less damage, as well as recovers 1/2 of your Constitution Modifier as health)\n\nand\n\n3) Constitution: Determines your health.\n\nIn the following selections, please use 1-3 for your choices.")
choice1 = 0
while choice1 == 0:
    primary = int(input("\nWhat do you want your Highest Stat to be?: "))
    if primary == 1 or primary == 2 or primary == 3:
        choice1 += 1
    else:
        print("\nPlease Try Again. \n")
        pass

choice2 = 0
while choice2 == 0:
    secondary = int(input("What do you want your Middle Stat to be?: "))
    if (secondary == 1 and secondary != primary) or (secondary == 2 and secondary != primary) or (
            secondary == 3 and secondary != primary):
        choice2 += 1
    else:
        print("\nPlease Try Again.\n")
        pass

choice3 = 0
while choice3 == 0:
    tertiary = int(input("What do you want your Lowest Stat to be?: "))
    if (tertiary == 1 and tertiary != primary and tertiary != secondary) or (
            tertiary == 2 and tertiary != primary and tertiary != secondary) or (
            tertiary == 3 and tertiary != primary and tertiary != secondary):
        choice3 += 1
    else:
        print("\nPlease Try Again.\n")
        pass

stats = {
    "Constitution": 0,
    "Intelligence": 0,
    "Strength": 0
}

if primary == 1:
    stats["Strength"] = 18 + random.randint(1, 2)
elif primary == 2:
    stats["Intelligence"] = 18 + random.randint(1, 2)
else:
    stats["Constitution"] = 18 + random.randint(1, 2)

if secondary == 1:
    stats["Strength"] = 14 + random.randint(1, 4)
elif secondary == 2:
    stats["Intelligence"] = 14 + random.randint(1, 4)
else:
    stats["Constitution"] = 14 + random.randint(1, 4)

if tertiary == 1:
    stats["Strength"] = 10 + random.randint(1, 4)
elif tertiary == 2:
    stats["Intelligence"] = 10 + random.randint(1, 4)
else:
    stats["Constitution"] = 10 + random.randint(1, 4)

print(
    "\nYou have rolled stats of:\nStrength = {Strength}, Intelligence = {Intelligence}, Constitution = {Constitution}\n".format(
        **stats))

str_mod = int((stats["Strength"] - 10) / 2)
print(f"Your Strength Modifier is: {str_mod}")
int_mod = int((stats["Intelligence"] - 10) / 2)
print(f"Your Intelligence Modifier is: {int_mod}")
con_mod = int((stats["Constitution"] - 10) / 2)
print(f"Your Constitution Modifier is: {con_mod}")
user_hp = 15 + (con_mod * 2)
print(f"\nYour Maximum Health is: {user_hp}")
initiative = int(1.5 * str_mod) + random.randint(1, 20)
print(f"\nYour Initiative is: {initiative}")

"This section allows the user to select 2 weapons that the user will use to fight the monster"

print(
    "\n\n\nYou will now be able to select 2 weapons from:\n\n1) Magic - Damage: 1d4 - Damage Type: 4\n2) Dagger - Damage: 1d4 - Damage Type: 2\n3) Shortsword - Damage: 1d6 - Damage Type: 3\n4) Warhammer - Damage: 1d8 - Damage Type: 1\n5) Pike - Damage: 1d10 - Damage Type: 2\n6) Greataxe - Damage: 1d12 - Damage Type: 3\n\nPlease Select a number 1-6 for each selection.")

choice4 = 0
while choice4 == 0:
    select_weapon_1 = int(input("\nWhat do you want for your First Weapon? : "))
    if select_weapon_1 == 1 or select_weapon_1 == 2 or select_weapon_1 == 3 or select_weapon_1 == 4 or select_weapon_1 == 5 or select_weapon_1 == 6:
        selected_weapon_1 = weapon_select(select_weapon_1)
        choice4 += 1
    else:
        print("\nPlease Try Again.\n")

choice5 = 0
while choice5 == 0:
    select_weapon_2 = int(input("What do you want for your Second Weapon? : "))
    if (
            select_weapon_2 == 1 or select_weapon_2 == 2 or select_weapon_2 == 3 or select_weapon_2 == 4 or select_weapon_2 == 5 or select_weapon_2 == 6) and (
            select_weapon_2 != select_weapon_1):
        selected_weapon_2 = weapon_select(select_weapon_2)
        choice5 += 1
    else:
        print("\nPlease Try Again.\n")
print("Weapon 1: Damage = {damage} Damage Type = {d_t}".format(**selected_weapon_1))
print("Weapon 2: Damage = {damage} Damage Type = {d_t}".format(**selected_weapon_2))
print()

"This section allows the user to select a difficulty tier of monster to fight"

choice6 = 0
while choice6 == 0:
    select_monster = int(input("\nWhat monster would you like to fight? Easy = 1, Medium = 2, Hard = 3: "))
    if select_monster == 1 or select_monster == 2 or select_monster == 3:
        selected_monster = mon_select(select_monster)
        print(
            "You have selected {name}\nHealth: {hp}, Damage: {damage}, Vulnerabilities: {d_v}, Resistances: {d_r}\n\n".format(
                **selected_monster))
        choice6 += 1
    else:
        print("\nPlease Try Again\n")

"Combat Section"
print(
    "\n\nYou will now enter combat with the selected enemy, you will have 3 choices of actions to take:\n\n1) Attack: You will be prompted to choose which weapon to attack with, after selecting, you will then automatically make an attack roll which will determine if you hit the monster, if you miss, your turn is over, and the enemy will attack, if you hit, you will roll damage from the weapon, and add your strength or intelligence modifier (depends on the weapon selected), the result is then done as damage to the opponent's health.\n\n2)Heal: You will recover an amount of Health equal to 1.5 times your constitution modifier (rounded down).\n\n3)Run: You will run away from the fight, and the game is over.\n\nNote: the goal of the game is to defeat the selected opponent by bringing their health to 0 or less, and if your health reaches 0 or less, then it is game over and you lose.")

# Good until here

heal_amount = int(1.5 * con_mod)

# following code that is blocked out in comments is possibly useless (depends on what i do for combat)
"""

def attack():
  weap_damage = {}
  if selected_weapon_1["d_t"] == 4:
    if selected_weapon_2["d_t"] == 4:
      weap_damage = {
        "w_1_damage" : random.randint(1,selected_weapon_1["damage"]) + int_mod,
        "w_2_damage" : random.randint(1,selected_weapon_2["damage"]) + int_mod
      }
    else:
      weap_damage = {
        "w_1_damage" : random.randint(1,selected_weapon_1["damage"]) + int_mod,
        "w_2_damage" : random.randint(1,selected_weapon_2["damage"]) + str_mod
      }

  else:
    if selected_weapon_2["d_t"] == 4:
      weap_damage = {
        "w_1_damage" : random.randint(1,selected_weapon_1["damage"]) + str_mod,
        "w_2_damage" : random.randint(1,selected_weapon_2["damage"]) + int_mod
      }
    else:
      weap_damage = {
        "w_1_damage" : random.randint(1,selected_weapon_1["damage"]) + str_mod,
        "w_2_damage" : random.randint(1,selected_weapon_2["damage"]) + str_mod
      }
  return weap_damage

"""

run = 0
while run == 0:
    if run != 0:
        break
    elif user_hp <= 0:
        print("You Lose. Your character has died.")
        break
    elif selected_monster["hp"] <= 0:
        print("You Win. The monster has been killed.")
        break
    else:
        pass
    choice7 = 0
    while choice7 == 0:
        action = int(input("\n\nWhat would you like to do?: "))
        if action == 1 or action == 2 or action == 3:
            choice7 += 1
        else:
            print("\nPlease Try Again.\n")
    if action == 3:
        print("You Lose. You ran away like a little baby.")
        run = 1
    elif action == 2:
        user_hp = user_hp + int(2 * con_mod)
        print(f"You have healed {heal_amount} damage, Health is now at {user_hp}")
    else:
        choice8 = 0
        while choice8 == 0:
            atk_with = int(input("Which weapon do you want to attack with?: "))
            if atk_with == 1 or atk_with == 2:
                choice8 += 1
            else:
                print("\nPlease Try Again.\n")
        if atk_with == 1:
            if selected_weapon_1["d_t"] == 4:
                user_hp += int(0.5 * int_mod)
                if selected_weapon_1["d_t"] == selected_monster["d_r"]:
                    selected_monster["hp"] -= 0.5 * (random.randint(1, selected_weapon_1["damage"]) + int_mod)
                elif selected_weapon_1["d_t"] == selected_monster["d_v"]:
                    selected_monster["hp"] -= 2 * (random.randint(1, selected_weapon_1["damage"]) + int_mod)
                else:
                    selected_monster["hp"] = selected_monster["hp"] - (
                                random.randint(1, selected_weapon_1["damage"]) + int_mod)
                print("\nThe monster is at {hp} Health remaining".format(**selected_monster))
            else:
                rand1 = random.randint(1, 20)
                if (rand1 + str_mod) >= selected_monster["armor"]:
                    if selected_weapon_1["d_t"] == selected_monster["d_r"]:
                        selected_monster["hp"] -= 0.5 * (random.randint(1, selected_weapon_1["damage"]) + str_mod)
                    elif selected_weapon_1["d_t"] == selected_monster["d_v"]:
                        selected_monster["hp"] -= 2 * (random.randint(1, selected_weapon_1["damage"]) + str_mod)
                    else:
                        selected_monster["hp"] = selected_monster["hp"] - (
                                    random.randint(1, selected_weapon_1["damage"]) + str_mod)
                        print("\nThe monster is at {hp} Health remaining".format(**selected_monster))
                else:
                    print("\nYou Missed\n")
        else:
            if selected_weapon_2["d_t"] == 4:
                user_hp += int(0.5 * int_mod)
                if selected_weapon_2["d_t"] == selected_monster["d_r"]:
                    selected_monster["hp"] -= 0.5 * (random.randint(1, selected_weapon_2["damage"]) + int_mod)
                elif selected_weapon_2["d_t"] == selected_monster["d_v"]:
                    selected_monster["hp"] -= 2 * (random.randint(1, selected_weapon_2["damage"]) + int_mod)
                else:
                    selected_monster["hp"] = selected_monster["hp"] - (
                                random.randint(1, selected_weapon_2["damage"]) + int_mod)
                print("\nThe monster is at {hp} Health remaining".format(**selected_monster))
            else:
                rand2 = random.randint(1, 20)
                if (rand2 + str_mod) >= selected_monster["armor"]:
                    if selected_weapon_2["d_t"] == selected_monster["d_r"]:
                        selected_monster["hp"] -= 0.5 * (random.randint(1, selected_weapon_2["damage"]) + str_mod)
                    elif selected_weapon_2["d_t"] == selected_monster["d_v"]:
                        selected_monster["hp"] -= 2 * (random.randint(1, selected_weapon_2["damage"]) + str_mod)
                    else:
                        selected_monster["hp"] = selected_monster["hp"] - (
                                    random.randint(1, selected_weapon_2["damage"]) + str_mod)
                        print("\nThe monster is at {hp} Health remaining".format(**selected_monster))
                else:
                    print("\nYou Missed\n")

    if run != 0:
        break
    elif user_hp <= 0:
        print("You Lose. Your character has died.")
        break
    elif selected_monster["hp"] <= 0:
        print("You Win. The monster has been killed.")
        break
    else:
        print("\n\nIt is now the Monsters turn to attack.\n")
        if random.randint(1, 20) >= 13:
            user_hp = user_hp - selected_monster["damage"]
            print(f"You are now at {user_hp} Health remaining\n")
        else:
            print("\nThe Monster missed\n")
            print(f"You are at {user_hp} Health remaining\n")

"This is the end of the code."