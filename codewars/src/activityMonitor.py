"""
-------------------------------------------------------
Activity Monitor
-------------------------------------------------------
Author:  JD
ID:      #
Email:   jsingh@live.com
__updated__ = "2023-05-27"
-------------------------------------------------------
"""
# Imports
from random import randint
from os import system
from time import sleep


dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")

}

def clear():
    system('clear')
    
def activity_marker(mode=1, frequency=.5):
    """----------------------------------------------------
    Dice Active Status Art
    Use: dice_art_loader(frequency=1)
    -------------------------------------------------------
    Parameters:
        frequency - refresh rate (int>0)  
    Returns:
        None
    ----------------------------------------------------"""
    print('\033[1;32m ')

    def single_step():
        dice = []
        clear()
        dice = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
        clear()
        for line in range(5):
            for die in dice:
                print(f'{dice_art.get(die)[line]} ', end='')
            print('')      

    if mode == 1:
        while True:
            single_step()
            sleep(frequency)
    else:
        single_step()
        print('')


activity_marker()