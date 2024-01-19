'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-10 11:25:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-10 11:25:30

@Title : Find the no of times a specified element occured in an array
'''

def count_occurences(arr,ele):
    count=0
    for i in arr:
        if i==ele:
            count+=1
    return count
arr=[1,5,3,8,91,234,22,16,16,54,32,5,8,9,2,91,0]
ele=int(input())
count=count_occurences(arr,ele)
print(f"The no of times {ele} occured in array is {count}")