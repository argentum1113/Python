"""
File: Steeplechase.py
Name: AVRIL
---------------------------------

"""

from karel.stanfordkarel import *


def main():
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    pre-condition:Karel is on the left, facing East.
    post-condition:Karel is on the right, facing East.

    """
    up()
    cross()
    down()

def up():
    """
    pre-condition:Karel is on the left, facing East.
    post-condition:Karel is on the top left, facing East.

    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()


def cross():
    """
    pre-condition:Karel is on the top left, facing East.
    post-condition:Karel is on the top right, facing South.

    """
    move()
    turn_right()


def down():
    """
    pre-condition:Karel is on the top right, facing South.
    post-condition:Karel is on the bottom right, facing East.

    """
    while front_is_clear():
        move()
    if not front_is_clear():
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
