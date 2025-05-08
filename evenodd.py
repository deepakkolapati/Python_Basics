'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 12:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 12:30:00

@Title : find the number is even or odd

'''





def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
num = 15
result = check_even_odd(num)
print(f"{num} is {result}")
