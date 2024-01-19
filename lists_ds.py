'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-10 02:25:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-10 02:25:30

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

def remove_duplicate(list):
    new_list=[]
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list





if __name__ == "__main__":
    print(sum([1,2,3,4,5]))

