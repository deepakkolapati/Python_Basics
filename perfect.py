'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 3:10:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 3:10:00

@Title : finding the nth term in fibonacci series

'''

def perfect_number(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return True
    return False
num=int(input())
if perfect_number(num):
    print(f"the {num} is a perfect number")
else:
    print(f"the {num} is not a perfect number")
