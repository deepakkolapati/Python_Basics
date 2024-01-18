'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 3:20:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 3:20:00

@Title : finding the nth term in fibonacci series

'''

def prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

num=int(input())
if prime(num):
    print(f"the {num} is a prime number")
else:
    print(f"the {num} is not a prime number")