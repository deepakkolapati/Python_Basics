'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 12:00:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 12:00:00

@Title : find the character is a vowel or consonant

'''



def check_vowel_consonant(char):
    vowels = "AEIOUaeiou"
    if char.isalpha():
        if char in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Not a valid alphabet"

# Example usage
alphabet = 'a'
result = check_vowel_consonant(alphabet)
print(f"{alphabet} is a {result}")
