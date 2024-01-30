'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-30 11:25:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-30 11:25:30

@Title : User Registration Problem
'''
import re
from logger import get_logger
log=get_logger()
class User:

    name_pattern = r'^[A-Z]+[a-zA-Z]{2,}$'
    email_pattern = r'^[a-z]+[\.[a-z]*]?@[a-z]{1,}\.[a-z]{2,}$'
    phno_pattern=r'^[0-9]{2,3} [0-9]{10}$'
    password_pattern = r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&]).{8,}$'
   
    def __init__(self, first_name, last_name, email, phno, password) -> None:
        self.__first_name  = self.first_name = first_name
        self.__last_name = self.last_name=last_name
        self.__email=self.email=email
        self.__phno=self.phno=phno
        self.__password=self.password=password

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        try:
            if self.check_password(password):
                self.__password = password
        except ValueError as e:
            log.error(e)
    
    def check_password(self, password):
        if re.match(self.password_pattern, password):
            return True    
        else: 
            raise ValueError(f'{password} is invalid')

    @property
    def phno(self):
        return self.__phno
    
    @phno.setter
    def phno(self,phno):
        try:
            if self.check_phno(phno):
                self.__phno = phno
        except ValueError as e:
            log.error(e)
    
    def check_phno(self, phno):
        if re.match(self.phno_pattern, phno):
            return True    
        else: 
            raise ValueError(f'{phno} is invalid')


    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email):
        try:
            if self.check_email(email):
                self.__email = email
        except ValueError as e:
            log.error(e)
    
    def check_email(self, email):
        if re.match(self.email_pattern, email):
            return True    
        else: 
            raise ValueError(f'{email} is invalid')

    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        try:
            if self.check_name(first_name):
                self.__first_name = first_name
        except ValueError as e:
            log.error(e)

    def check_name(self, name):
        if re.match(self.name_pattern, name):
            return True    
        else: 
            raise ValueError(f'{name} is invalid')

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        try:
            if self.check_name(last_name):
                self.__last_name = last_name
        except ValueError as e:
            log.error(e)
        

    
if __name__=="__main__":
    u1=User("Deepak","Chandu","deepk@gmail.c","91 799779989","bcd$dfgdfg1")
    

        
         