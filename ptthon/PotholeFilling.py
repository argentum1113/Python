"""
File: PotholeFilling.py
Name: AVRIL
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""
from karel.stanfordkarel import *

def main():
    while front_is_clear():
        go_in()
        put_beeper()
        go_out()
        move()


def go_in():
    """
    pre-condition:Karel is at the upper left of the pothole, facing East.
    post-condition:Karel is in the pothole, facing South.
    :return:
    """
    move()
    turn_right()
    move()

def go_out():
    """
    pre-condition:Karel is in the pothole, facing South.
    post-condition:Karel is on the top of the pothole, facing East.
    :return:
    """
    turn_around()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def put99():
    for i in range(99):
        put_beeper()

def turn_around():
    for i in range(2):
        turn_right()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
_karel_task(main)
