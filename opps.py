'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-25 11:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-25 11:30:00

@Title : OOPS in Python

'''

class Person:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.__age=age
    
    def get_fullname(self):
        return f"{self.fname} {self.lname}"

    def introduce(self):
        return f"Hii.I'm {self.fname} {self.lname}.I'm {self.__age}yrs old"

    @classmethod
    def annonymous(cls):
        return Person("Iron","Man",40)



    
if __name__=="__main__":
     p=Person.annonymous()
     print(p.introduce())