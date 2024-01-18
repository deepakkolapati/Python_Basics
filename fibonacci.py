'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 2:10:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 2:10:00

@Title : finding the nth term in fibonacci series

'''
def fibonacci(num):
    if num==1 or num==2:
        return num-1
    num1=0
    num2=1
    for i in range(2,num):
        num3=num2+num1
        num1=num2
        num2=num3
    return num2
num=int(input())
fibnum=fibonacci(num)
print(f"the {num}th term of fibonnaci series is {fibnum}")