'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-20 11:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-20 11:30:00

@Title : Creating Employee Wage Program

'''
import random

        
class Employee:
    def __init__(self,name,wage_per_hour,full_day_hour,part_time_hour,no_of_days,no_of_hours):
        self.name=name
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
        return self.hours,self.wage,self.days
            

class Company:
    def __init__(self,company_name):
        self.company_name=company_name
        self.emplyoee_dict={}

    def add(self,emp):
        if emp.name not in self.emplyoee_dict:
            self.emplyoee_dict[emp.name]=emp

    def display(self,employee_name):
        if employee_name in self.emplyoee_dict:
           emp=self.emplyoee_dict[employee_name]
           print(f"{emp.name} worked for {emp.days} days {emp.hours} hours his monthly wage is {emp.wage}")
        else:
            print("Employee not found")
    
    def update(self,employee_name,wage_per_hour):
        if employee_name in self.emplyoee_dict:
            self.emplyoee_dict[employee_name].wage_per_hour=wage_per_hour
        

    def delete(self,employee_name):
        if employee_name in self.emplyoee_dict:
            del self.emplyoee_dict[employee_name]
        else:
            print("Employee not found")
    



def main():
    print("Welcome to Employee Wage problem")
    # emp1=Employee("Deepak",20,8,3,20,100)
    # emp2=Employee("Joshi",20,8,3,20,100)
    # # emp1.calculate_monthly_wage()
    # # print(f"The employee worked for {emp1.days} days {emp1.hours} hours his monthly wage is {emp1.wage}")
    # cmp1=Company("Tcs")
    # cmp1.add(emp1)
    # cmp1.display("Deepak")
    # print("****************************************************")
    # cmp1.add(emp2)
    # cmp1.display("Joshi")
    # print("****************************************************")
    # cmp1.delete("Deepak")
    # cmp1.display("Deepak")
    # print("****************************************************")
    # cmp1.update("Joshi",25)
    # cmp1.display("Joshi")
    # print("****************************************************")
    # cmp1.delete("Joshi")
    # cmp1.display("Joshi")

    company = Company('ABC')
    while True:
        choice = int(input('Enter 1 to add, 2 to update, 3 to display, 4 to delete : '))
        if choice == 1:
            employee_name=input("Enter the employee_name: ")
            wage_per_hour=int(input("Enter the wage_per_hour: "))
            full_day_hour=int(input("Enter the full_day_hour: "))
            part_time_hour=int(input("Enter the part_time_hour: "))
            no_of_days=int(input("Enter the no_of_days: "))
            no_of_hours=int(input("Enter the no_of_hours: "))
            employee = Employee(employee_name,wage_per_hour,full_day_hour,part_time_hour,no_of_days,no_of_hours)
            employee.calculate_monthly_wage()
            company.add(employee)
        elif choice==2:
            employee_name=input("Enter the employee_name: ")
            new_wage=input("Enter the new wage_per_hour: ")
            company.update(employee_name,new_wage)
        elif choice ==3:
            employee_name=input("Enter the employee_name: ")
            company.display(employee_name)
        elif choice==4:
            employee_name=input("Enter the employee_name: ")
            company.delete(employee_name)
        else:
            break



if __name__=="__main__":
    main()
    