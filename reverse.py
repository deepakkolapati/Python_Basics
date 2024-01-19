'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-10 11:14:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-10 11:14:30

@Title : Reverse the elements in an array
'''

def reverse(arr):
    length=len(arr)
    if length==0:
        return arr
    mid=length//2
    for i in range(0,mid+1):
        arr[i],arr[length-i-1]=arr[length-i-1],arr[i]
    return arr
array=[1,2,3,4,5,6,7]
array=reverse(array)
for i in array:
    print(i)

