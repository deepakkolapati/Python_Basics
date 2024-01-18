'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 11:40:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 11:40:00

@Title : Find the year entered is leap year or not

'''


year=0
while True:
    year=input("Enter the year :")
    if len(year)==4:
        break
    else:
        print("Enter the correct year")
year=int(year)
if (year%4==0 and year%100!=0):
    print("It's a leap year")
elif (year%400==0):
    print("It's a leap year")
else:
    print("It's not a leap year")
