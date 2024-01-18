'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 11:50:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 11:50:00

@Title : printing all the 2^i numbers are leap years or not where i runs from 0 to the given input N

'''
def checkleapyear(year):

    if ((year%4==0 and year%100!=0)or(year%400==0)):
        return True
    else:
        return False
n=int(input("Enter a number less than 31: "))
for i in range(n+1):
    year=2**i
    print(year,end=" ")
    if checkleapyear(year):
        print("it's a leap year")
    else:
        print("it's not a leap year")
    
