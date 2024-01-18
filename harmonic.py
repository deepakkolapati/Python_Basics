'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 12:00:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 12:00:00

@Title : print the nth harmonic number

'''
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=1/(i)

print(sum,"is the ",n,"th harmonic number")
