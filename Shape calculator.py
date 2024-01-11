"""
File: TristanWijnmaalen_FinalProject.py
07/26/2023
Final Project for Intro to Python

Provides a menu-driven tool for calculating areas/circumferences/perimeters of shapes and showing the formula used.
"""

import math, time

QUIT = '7'

COMMANDS = ('1', '2', '3', '4', '5', '6', '7')  # Using tuples for menus

STUFF = ('1', '2', '3')

THINGS = ('1', '2')

MENU = """Tristan's Shape Machine
1   Circle
2   Rectangle
3   Triangle
4   Rhombus
5   Trapezoid
6   Hexagon
7   Quit the program"""
MENU2 = """1   Formula
2   Calculate\n"""


def main():
    # Loops the user so they're able to use the program until they enter the quit command.
    while True:
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Have a nice day!")
            time.sleep(
                2)  # Pauses the program for 2 seconds before closing so the user can read the heartwarming message. (For anyone that might run this with a double-click, doesn't matter with an F5 in the IDLE)
            break


def acceptCommand():
    # Asks the user to input a command and then returns the command.
    while True:
        command = input("Enter a command number: ")
        if not command in COMMANDS:
            print("Error: command not recognized")
        else:
            return command


def runCommand(command):
    # This function is a routing center. Using the value of 'command', the appropriate function is called.
    if command == '1':
        req = float(input("Enter the radius of the circle: "))
        Circle(req)
    elif command == '2':
        req1 = float(input("Enter the length of the base of the rectangle: "))
        req2 = float(input("Enter the length of the height of the rectangle: "))
        Rectangle(req1, req2)
    elif command == '3':
        req1 = float(input("Enter the length of the base of the triangle: "))
        req2 = float(input("Enter the length of the height of the triangle: "))
        Triangle(req1, req2)
    elif command == '4':
        req1 = float(input("Enter the length of the first diagonal of the rhombus: "))
        req2 = float(input("Enter the length of the second diagonal of the rhombus: "))
        Rhombus(req1, req2)
    elif command == '5':
        req1 = float(input("Enter the length of the first base of the trapezoid: "))
        req2 = float(input("Enter the length of the second base of the trapezoid: "))
        req3 = float(input("Enter the length of the height of the trapezoid: "))
        Trapezoid(req1, req2, req3)
    elif command == '6':
        req = float(input("Enter the length of the sides of the hexagon: "))
        Hexagon(req)


def Circle(radius):
    # Calculates either the area or circumference and can also print the respective formula.
    MENU1 = "\nCircle with a radius of " + str(radius) + """
1   Area
2   Circumference
3   Back to Main Menu\n"""
    while True:
        ch1 = input(MENU1 + "Enter a command number: ")
        if not ch1 in STUFF:
            print("Error: command not recognized")
        elif ch1 == '1':
            ch2 = input("Area\n" + MENU2 + "Enter a command number: ")
            if not ch2 in THINGS:
                print("Error: command not recognized")
            elif ch2 == '1':
                print("The formula used to calculate the area of a circle in this program is math.pi*" + str(
                    radius) + "**2")
            else:
                area = round(math.pi * radius ** 2, 2)
                print("The area of the circle is " + str(area) + ". (Rounded to 2 decimal places)")
        elif ch1 == '2':
            ch2 = input("Circumference\n" + MENU2 + "Enter a command number: ")
            if not ch2 in THINGS:
                print("Error: command not recognized")
            elif ch2 == '1':
                print("The formula used to calculate the circumference of a circle in this program is math.pi*(" + str(
                    radius) + "*2)")
            else:
                circumference = round(math.pi * (radius * 2), 2)
                print("The circumference of the circle is " + str(circumference) + ". (Rounded to 2 decimal places)")
        else:
            break


def Rectangle(base, height):
    # Calculates either the area or perimeter and can also print the respective formula.
    MENU1 = "\nRectangle with a base of " + str(base) + " and a height of " + str(height) + """
1   Area
2   Perimeter
3   Back to Main Menu\n"""
    while True:
        ch1 = input(MENU1 + "Enter a command number: ")
        if not ch1 in STUFF:
            print("Error: command not recognized")
        elif ch1 == '1':
            ch2 = input("Area\n" + MENU2 + "Enter a command number: ")
            if not ch2 in THINGS:
                print("Error: command not recognized")
            elif ch2 == '1':
                print(
                    "The formula used to calculate the area of a rectangle in this program is " + str(base) + "*" + str(
                        height))
            else:
                area = round(base * height, 2)
                print("The area of the rectangle is " + str(area) + ". (Rounded to 2 decimal places)")
        elif ch1 == '2':
            ch2 = input("Perimeter\n" + MENU2 + "Enter a command number: ")
            if not ch2 in THINGS:
                print("Error: command not recognized")
            elif ch2 == '1':
                print("The formula used to calculate the perimeter of a rectangle in this program is " + str(
                    base) + "*2+" + str(height) + "*2")
            else:
                perimeter = round(base * 2 + height * 2, 2)
                print("The perimeter of the rectangle is " + str(perimeter) + ". (Rounded to 2 decimal places)")
        else:
            break


def Triangle(base, height):
    # Calculates and gives area or shows formula used.
    while True:
        ch1 = input("Triangle with a base of " + str(base) + " and a height of " + str(
            height) + "\nArea\n" + MENU2 + "3   Back to Main Menu\nEnter a command number: ")
        if not ch1 in STUFF:
            print("Error: command not recognized")
        elif ch1 == '1':
            print("The formula used to calculate the area of a triangle in this program is " + str(base) + "*" + str(
                height) + "/2")
        elif ch1 == '2':
            area = round(base * height / 2, 2)
            print("The area of the triangle is " + str(area) + ". (Rounded to 2 decimal places)")
        else:
            break


def Rhombus(dia1, dia2):
    # Calculates and gives area or shows formula used.
    while True:
        ch1 = input("Rhombus with a diagonal of " + str(dia1) + " and another diagonal of " + str(
            dia2) + "\nArea\n" + MENU2 + "3   Back to Main Menu\nEnter a command number: ")
        if not ch1 in STUFF:
            print("Error: command not recognized")
        elif ch1 == '1':
            print("The formula used to calculate the area of a rhombus in this program is " + str(dia1) + "*" + str(
                dia2) + "/2")
        elif ch1 == '2':
            area = round(dia1 * dia2 / 2, 2)
            print("The area of the rhombus is " + str(area) + ". (Rounded to 2 decimal places)")
        else:
            break


def Trapezoid(base1, base2, height):
    # Calculates and gives area or shows formula used.
    while True:
        ch1 = input("Trapezoid with a first base of " + str(base1) + ", a second base of " + str(
            base2) + ", and a height of " + str(
            height) + "\nArea\n" + MENU2 + "3   Back to Main Menu\nEnter a command number: ")
        if not ch1 in STUFF:
            print("Error: command not recognized")
        elif ch1 == '1':
            print("The formula used to calculate the area of a trapezoid in this program is (" + str(base1) + "+" + str(
                base2) + ")/2*" + str(height))
        elif ch1 == '2':
            area = round((base1 + base2) / 2 * height, 2)
            print("The area of the trapezoid is " + str(area) + ". (Rounded to 2 decimal places)")
        else:
            break


def Hexagon(side):
    # Calculates and gives area or shows formula used.
    while True:
        ch1 = input("Hexagon with a side of " + str(
            side) + "\nArea\n" + MENU2 + "3   Back to Main Menu\nEnter a command number: ")
        if not ch1 in STUFF:
            print("Error: command not recognized")
        elif ch1 == '1':
            print("The formula used to calculate the area of a hexagon in this program is 3*math.sqrt(3)/2*" + str(
                side) + "**2")
        elif ch1 == '2':
            area = round(3 * math.sqrt(3) / 2 * side ** 2, 2)
            print("The area of the hexagon is " + str(area) + ". (Rounded to 2 decimal places)")
        else:
            break


main()