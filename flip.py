'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 11:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 11:30:00

@Title : To find the percentage of head and tails when u flip a coin N number of times

'''

import random
flips = int(input("How many times we should flip the coin:"))
heads=0
tails=0
for i in range(flips):
    probability= random.randint(0,1)
    if probability>0.5:
        heads+=1
    else:
        tails+=1
headspercent= heads/(heads+tails)
tailspercent=tails/(heads+tails)
print("The perecentage of heads is ",headspercent," the percentage of tails is ",tailspercent)
