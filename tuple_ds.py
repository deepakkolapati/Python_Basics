'''

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-01-10 03:14:30

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-01-10 03:14:30

@Title :  Tuple datastructures
'''

def create_tuple():
    return (1,2,3)

def create_diff_tuple():
    return ('a',24,"mango",[1,2])

def delete_char(tup,char):
    newtup=tuple(i for i in tup if i!=char)
    return newtup

def check_char(tup,char):
    if char in tup:
        return True
    
def list_to_tuple(list):
    return tuple(list)

if __name__=="__main__":
    tup1=(1,2,3,3,2,6,7,2,1)
    print(tup1[2:5])
    rev_tup=tuple(reversed(tup1))
    print(rev_tup)
    print(delete_char(tup1,2))
     

