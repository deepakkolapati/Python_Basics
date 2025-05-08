'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 12:10:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 12:10:00

@Title : Find all the prime factors of N

'''

def check_prime(num):
    if num==1 or num==2:
        return True
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def get_prime_factors(num):
    i=1
    while(i*i<=num):
        if num%i==0 and check_prime(i):
            print(i," is a prime factor of ", num)
        i+=1

num=int(input("Enter a number: "))
get_prime_factors(num)