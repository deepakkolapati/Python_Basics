'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 12:20:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 12:20:00

@Title : print the quotient and remainder of a number when divided by another number

'''
def compute_quotient_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# Example usage
dividend = 27
divisor = 4
q, r = compute_quotient_remainder(dividend, divisor)
print(f"Quotient: {q}, Remainder: {r}")

