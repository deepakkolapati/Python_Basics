'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-19 02:25:30

@Last Modified by : Kolapati Mani Deepak Chandu
    

@Last Modified time: 2024-01-19 02:25:30

@Title : Lists datastructures
'''

def sum(list):
    sum=0
    for i in list:
        sum+=i
    return sum

def mul(list):
    mul=1
    for i in list:
        mul*=i
    return mul

def min(list):
    if len(list)==0:
        return -1
    min=list[0]
    for i in list:
        if min>i:
            min=i
    return min
def count_first_and_last(list,len):
    count=0
    for i in list:
        if len(i)>2 and i[0]==i[-1]:
            count+=1
    return count

def clone(list):
    return list.copy()

def remove_duplicates(list):
    new_list=[]
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

def count_longer(list,n):
    count=0
    for str in list:
        if len(str)>n:
            count+=1
    return count

def one_common(list1,list2):
    for i in list1:
        if i in list2:
            return True
    return False
def append(list1,list2):
    list3=list1
    list3.extend(list2)
    return list3


if __name__ == "__main__":
    list=[1,2,3,2,1,4,5,6,4,3,2]
    print(sum(list))
    print(mul(list))
    print(min(list))
    print(clone(list))
    print(remove_duplicates(list))
    newlist=["apple","banana","guava","lemon","orange","water melon"]
    print(count_longer(newlist,6))
    print(one_common([1,2,3,4,5],[6,7,7,8,2]))
    print(append([1,2,3,4,5],[6,7,7,8,2]))