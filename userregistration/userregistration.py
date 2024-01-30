'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-30 11:25:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-30 11:25:30

@Title : User Registration Problem
'''
import re


def check_name(name):
   
    if len(name)<3:
        return False
    if not name[0].isupper():
        return False
    return True


    
if __name__=="__main__":
    fname=input("Enter The first name :")
    while not check_name(fname):
        fname=input("Enter The first name :")
    lname=input("Enter The last name :")
    while not check_name(lname):
        lname=input("Enter The last name :")
    print(fname+lname)
        
         