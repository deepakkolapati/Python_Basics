'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 12:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 12:30:00

@Title : Swap thegiven numbers

'''



def swap_numbers(a, b):
    a, b = b, a
    return a, b

# Example usage
num1 = 5
num2 = 10
num1, num2 = swap_numbers(num1, num2)
print(f"After swapping: num1 = {num1}, num2 = {num2}")
