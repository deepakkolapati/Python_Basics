'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-20 11:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-20 11:30:00

@Title : Creating Employee Wage Program

'''
import random

        
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
    
    @staticmethod
    def check_attendance():
        attendance_type=random.randint(0,2)
        return attendance_type
    
    def caluclate_daily_wage(self):
        self.attendance=self.check_attendance()
        match self.attendance:
            case 2:
                return self.full_day_hour
            case 1:
                return self.part_time_hour
            case 0:
                return 0
            
    def calculate_monthly_wage(self):
        
        while self.days<self.no_of_days and self.hours<self.no_of_hours:
            self.days += 1
            self.hours+=self.caluclate_daily_wage()
            
        self.wage = self.hours * self.wage_per_hour
            


def main():
    print("Welcome to Employee Wage problem")
    emp1=Employee(20,8,3,20,100)
    emp1.calculate_monthly_wage()
    print(f"The employee worked for {emp1.days} days {emp1.hours} hours his monthly wage is {emp1.wage}")

if __name__=="__main__":
    main()
    