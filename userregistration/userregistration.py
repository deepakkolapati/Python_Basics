'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-30 11:25:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-30 11:25:30

@Title : User Registration Problem
'''
import re

class User:

    name_pattern = r'^[A-Z]+[a-zA-Z]{2,}$'
    

    def __init__(self, first_name, last_name) -> None:
        self.first_name = self.fname = first_name
        self.last_name = self.lname = last_name

    @property
    def fname(self):
        return self.first_name
    
    def check_name(self, name):
        if re.match(self.name_pattern, name):
            return True    
        else: 
            raise ValueError(f'{name} is invalid')
    
    @fname.setter
    def fname(self, first_name):
        try:
            if self.check_name(first_name):
                self.first_name = first_name
        except ValueError as e:
            print(e)

    @property
    def lname(self):
        return self.last_name

    @lname.setter
    def lname(self, last_name):
        try:
            if self.check_name(last_name):
                self.last_name = last_name
        except ValueError as e:
            print(e)
        

    
if __name__=="__main__":
    user = User('Dee', 'Cha')

        
         