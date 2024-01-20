'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-20 11:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-20 11:30:00

@Title : Creating Employee Wage Program

'''
import random

def check_attendance() -> int: 
    """ generates a random integer between 0 and 1
    
    params: None
    Return: int
    """
    
    is_present = random.randint(0,1)
    return True if is_present == 1 else False

def caluclate_wage(wage_per_hour=8,full_day_hour=8) -> int:
    """ Caluclates the wage of the employee per day
    
    params: wage_per_hour,full_day_hour,is_present
    Return: int
    """
    is_present=check_attendance()
    if is_present:
       return wage_per_hour*full_day_hour
    
    return 0
    

def main():
    print("Welcome to Employee Wage problem")
    print(f"The employees wage is {caluclate_wage()}")


if __name__=="__main__":
    main()
    