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
        monthly_wage+=caluclate_daily_wage()
    return monthly_wage

def wage_computation(no_of_days=20,no_of_hours=100,full_day_hour=8,part_time_hour=3,wage_per_hour=20):
    days=0
    hours=0
    wage=0
    while days<no_of_days and hours<no_of_hours:
        employee_status=check_attendance()
        match employee_status:
            case 2:
                days+=1
                hours+=full_day_hour
                wage+=full_day_hour*wage_per_hour
                  
            case 1: 
                days+=1
                hours+=part_time_hour
                wage+=part_time_hour*wage_per_hour
                
                   
            case 0:
                  continue
                
    return days,hours,wage
           
class Employee:
    def __init__(self,wage_per_hour,full_day_hour,part_time_hour,no_of_days,no_of_hours):
        self.wage_per_hour=wage_per_hour
        self.full_day_hour=full_day_hour
        self.part_time_hour=part_time_hour
        self.no_of_days=no_of_days
        self.no_of_hours=no_of_hours
        self.days=0
        self.hours=0
        self. wage=0
    def check_attendance(self):
        attendance_type=random.randint(0,2)
        return attendance_type
    
    def caluclate_daily_wage(self):
        self.attendance=self.check_attendance()
        match self.attendance:
            case 2:
                return self.wage_per_hour*self.full_day_hour
            case 1:
                return self.wage_per_hour*self.part_time_hour
            case 0:
                return 0
    def calculate_monthly_wage(self):
        
        while self.days<self.no_of_days and self.hours<self.no_of_hours:
            self.attendance=self.check_attendance()
            match self.attendance:
               case 2:
                  self.days+=1
                  self.hours+=self.full_day_hour
                  self.wage+=self.full_day_hour*self.wage_per_hour
                  
               case 1: 
                  self.days+=1
                  self.hours+=self.part_time_hour
                  self.wage+=self.part_time_hour*self.wage_per_hour
                
                
        return self.days,self.hours,self.wage

                  
          




def main():
    print("Welcome to Employee Wage problem")
    emp1=Employee(20,8,3,20,100)
    days,hours,wage=emp1.calculate_monthly_wage()
    print(f"The employee worked for {days} days {hours} hours his monthly wage is {wage}")

if __name__=="__main__":
    main()
    