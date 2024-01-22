'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-22 16:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-22 16:30:00

@Title : Creating LineComparision Program

'''
import math
class Line:
    
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def get_Length(self):
        return math.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)
    def __eq__(self,other):
        return self.get_Length()==other.get_Length()
    def __lt__(self,other):
        return self.get_Length()<other.get_Length()
    def __gt__(self,other):
        return self.get_Length()>other.get_Length()
    
if __name__=="__main__":
        line1=Line(2,5,3,4)
        line2=Line(2,5,3,4)
        line3=Line(3,4,10,8)
        line4=Line(3,1,4,4)
        line5=Line(5,2,6,10)
        line6=Line(3,4,10,8)
        lines=[line1,line2,line3,line4,line5]

        for i in range(len(lines)-1):
            for j in range(i+1,len(lines)):
                if lines[i]==lines[j]:
                    print(f"{lines[i]} is equal to {lines[j]}")
                if lines[i]>lines[j]:
                    print(f"{lines[i]} is greater than {lines[j]}")
                if lines[i]<lines[j]:
                    print(f"{lines[i]} is less than {lines[j]}")
        



    