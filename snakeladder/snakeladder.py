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
    extra_chance=True
    while extra_chance and player_position!=100:
        option=random.choice(options)
        if option=="snake":
            player_position-=dice
            if player_position<0:
                player_position=0
            extra_chance=False
            
        elif option=="ladder":
            if player_position+dice<=100:
                player_position+=dice
        else:
            extra_chance=False

        
    return player_position


if __name__=="__main__":
    print("Welcome to the Snake and Ladder Program")
    player1_position=0
    player2_position=0
    player=0
    dice_count=0
    while player1_position!=100 and player2_position!=100:
        if player==0:
            player1_position=roll_dice(player1_position)
        if player==1:
            player2_position=roll_dice(player2_position)
        dice_count+=1
        if player1_position==100:
            print("Player 1 won the game")
            break
        if player2_position==100:
            print("Player 2 won the game")
            break
        player=(player+1)%2
    print(f"The dice rolled for {dice_count} times")




