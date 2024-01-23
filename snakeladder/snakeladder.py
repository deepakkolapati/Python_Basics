'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-23 10:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-23 10:30:00

@Title : Creating Snake Ladder Program

'''
import random

player_position=0

def roll_dice():
    return random.randint(1,6)

def check_option():
    options=["snake","ladder","no play"]
    option=random.choice(options)
    return option

if __name__=="__main__":
    print(roll_dice())
    print(check_option())