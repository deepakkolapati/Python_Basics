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
    
    is_present =random.randint(0,2)
    return is_present

def caluclate_daily_wage(wage_per_hour=8,full_day_hour=8,part_time_hour=4) -> int:
    """ Caluclates the wage of the employee per day
    
    params: wage_per_hour,full_day_hour,part_time_hour
    Return: int
    """
    is_present=check_attendance()
    match is_present:
        case 2:
            return wage_per_hour*full_day_hour
        case 1: 
            return wage_per_hour*part_time_hour
        case 0:
            return 0
    
def calculate_monthly_wage(no_of_days=20) -> int:
    """ Caluclates the wage of the employee per month
    
    params: no_of_days
    Return: int
    """
    
    monthly_wage=0
    for i in range(no_of_days):
        monthly_wage+=caluclate_daily_wage
    return monthly_wage

def main():
    print("Welcome to Employee Wage problem")
    print(f"The employees wage is {caluclate_daily_wage()}")


if __name__=="__main__":
    main()
    