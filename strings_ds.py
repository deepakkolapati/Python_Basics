'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-20 10:14:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-20 10:14:30

@Title :  String datastructures
'''

def length(str):
    count=0
    for i in str:
        count+=1
    return count

def character_frequency(str):
    str=str.lower()
    frequency=[0]*26
    dict={}
    for i in str:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
    return dict

def add_ing_ly(str):
     if len(str)<3:
          return str
     if str[len(str)-3:]=="ing":
          str2=str+"ly"
          return str2
     else:
          return str+"ing"
     
def largest_all(list):
    largeindex=0
    largelength=0
    count=0
    for str in list:
        if len(str)>largelength:
            largelength=len(str)
            largeindex=count
        count+=1
    return list[largeindex]

def seperate(str):
    li=list(str.split(','))
    return li
def change_first_occur(str,char):
    flag=0
    newstr=""
    count=0
    for i in str:
        if i==char and flag==1:
              newstr+="$"
        elif i==char and flag==0:
              newstr+=char
              flag=1
        else:
            newstr+=str[count]
        count+=1
    return newstr
        
         
def reverse(str):
     newstr=str[::-1]
     return newstr

def display_up_low():
     str=input("Enter a string in both upper and lower case: ")
     print(str.upper())
     print(str.lower())

def lower_first_n(str,n):
     if n>len(str):
          return str
     newstr=str[:n].lower()+str[n:]
     return newstr

def count_occurences(str,char):
     return str.count(char)

if __name__=="__main__":
    str="abcdabcdefijkndsfufwiwiniwnngkwnw"
    print(character_frequency(str))
    str="eating"
    print(add_ing_ly(str))
    lists=["apple","banana","guava","water melon"]
    print(largest_all(lists))
    display_up_low()
    print(seperate("hii,how r u,i'm fine,where r u from,k bye"))
    print(reverse("abcd"))
    print(lower_first_n("ABCDnffHVHDVBVifhdj",10))
    print(change_first_occur("abcddhgsfhvhjcubchvhwiowkbcbdbc",'b'))
    print(count_occurences("hii hii how r u k k how is the weather bye ","how"))
    