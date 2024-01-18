'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 3:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 3:30:00

@Title : finding the nth term in fibonacci series

'''

def reverse(num):
    reversenum=0
    while(num>0):
        remainder=num%10
        reversenum=reversenum*10+remainder
        num=num//10
    return reversenum
num=int(input())
rnum=reverse(num)
print(f"The reversed number of {num} is {rnum}")
   