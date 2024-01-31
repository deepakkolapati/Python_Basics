'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-31 01:14:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-31 01:14:30

@Title : Implement Sorting

'''

import sys
sys.setrecursionlimit(10000)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
    
def merge_sort(arr,left,right):
    if left<right:
        
        mid=left+(right-left)//2
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        merge(arr,left,mid,right)

def merge(arr,left,mid,right):
    
    list1=[]
    list2=[]
   
    for i in range(left,mid+1):
        list1.append(arr[i])

    for j in range(mid+1,right+1):
        list2.append(arr[j])
    left_index=mid-left+1
    right_index=right-mid
    i=0
    j=0
    index=left
    while i<left_index and j<right_index:
        if list1[i]<list2[j]:
            arr[index]=list1[i]
            i+=1
            index+=1
        else:
            arr[index]=list2[j]
            j+=1
            index+=1
    while i<left_index:
        arr[index]=list1[i]
        i+=1
        index+=1
    while j<right_index:
        arr[index]=list2[j]
        j+=1
        index+=1


if __name__=="__main__":
    arr=[4,3,2,1,6,7,15,12,11,17,13]
    # bubble_sort(arr)
    length=len(arr)-1
    merge_sort(arr,0,length-1)
    print(arr)
