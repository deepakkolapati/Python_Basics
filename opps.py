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
        return f"Hii. I'm {self.fname} {self.lname}. I'm {self.__age}yrs old."
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self.__age=age
    
    def __lt__(self,other):
        return self.__age< other.get_age()
    
    def __gt__(self,other):
        return self.__age> other.get_age()
    
    def __eq__(self,other):
        return self.__age== other.get_age()

    @classmethod
    def annonymous(cls):
        return cls("Iron","Man",40)


class Student(Person):
    schoolname="ABC"
    def __init__(self,fname,lname,age,marks):
        # Person.__init__(self, fname,lname,age)
        super().__init__(fname, lname, age)
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self,marks):
        self.__marks=marks

    def introduce(self):
        return super().introduce()+ f" Im studying in {self.schoolname} school"
    
    @classmethod
    def annonymous(cls):
        # return super().annonymous()
        return cls('deepak', 'chandu', 22, 100)
    
    

if __name__=="__main__":
    p=Person.annonymous()
    print(p.introduce())
    s=Student("vvs","sudheer",21,950)
    print(s.introduce())
    s2=Student.annonymous()
    print(s2.introduce())
    print(s2.introduce())