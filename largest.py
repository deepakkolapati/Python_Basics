'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 12:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 12:30:00

@Title : Find the largest of all the 3 numbers

'''





def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

# Example usage
a = 15
b = 27
c = 10
largest = find_largest(a, b, c)
print(f"The largest among {a}, {b}, and {c} is: {largest}")
