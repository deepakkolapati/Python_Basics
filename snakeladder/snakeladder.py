'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-23 10:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-23 10:30:00

@Title : Creating Snake Ladder Program

'''
import random



def roll_dice(player_position):
    dice=random.randint(1,6)
    options=["snake","ladder","no play"]
    option=random.choice(options)
    if option=="snake":
        player_position-=dice
        if player_position<0:
            player_position=0
    if option=="ladder":
        if player_position+dice<=100:
           player_position+=dice
    return player_position


    
    
    

if __name__=="__main__":
    player_position=0
    print("The player is at position 0")
    while player_position<100:
      player_position=roll_dice(player_position)
      print(f"PLayer is at position {player_position}")