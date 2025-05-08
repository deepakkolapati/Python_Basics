'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-19 11:25:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-19 11:25:30

@Title :  Array datastructures
'''

def print_array(arr):
    n=len(arr)
    print("[",end='')
    for i in range(n-1):
        #print(f"The element in index {i} of array is {arr[i]}")
        print(arr[i],end=',')
    print(f"{arr[n-1]}]")
    
def reverse(arr):
    to_rev = arr
    length=len(to_rev)
    if length==0:
        return to_rev
    mid=length//2
    for i in range(0,mid+1):
        to_rev[i],to_rev[length-i-1]=to_rev[length-i-1],to_rev[i]
    return to_rev

def count_occurences(arr,ele):
    count=0
    for i in arr:
        if i==ele:
            count+=1
    return count
def delete_first_occurence(arr,ele):
    new_arr=arr
    n=len(new_arr)
    flag=1
    i=0
    for i in range(n):
        if new_arr[i]==ele and flag==1 and i!=n-1:
            flag=0
            new_arr[i]=new_arr[i+1]
        elif flag==0 and i!=n-1:
            new_arr[i]=new_arr[i+1]
        else:
            continue
    if (flag==1 and new_arr[n-1]==ele) or (flag==0) :
        new_arr.pop()
    
    return new_arr
            

if __name__=="__main__":
    arr=[1,5,3,4,3,2,1]
    print_array(arr)
    reversearray=reverse(arr)
    print("The reverse array is ")
    print_array(reversearray)
    ele=int(input("Enter the number to count occurences: "))
    count=count_occurences(arr,ele)
    print(f"The no of times {ele} occured in array is {count}")
    ele=int(input("Enter the number to be deleted: "))
    deleted_array=delete_first_occurence(arr,ele)
    print(deleted_array)
