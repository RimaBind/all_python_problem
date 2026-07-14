#Don't return early here because I need to collect all valid pairs,
#not just the first  even-product pair

def pair_with_even_sum(num):
    n=len(num)
    res=[]
    for i in range(n):
        for j in range(1+i,n):
            if num[i]*num[j]%2==0:
                res.append([num[i],num[j]])
    
    return res
"""
def second_largest(sorted):#if I give sorted list 
    size=len(sorted)
    return sorted[size-2]

"""

def second_largest_unsorted(unsorted): # if I give  unsorted list 
     size=len(unsorted)
     unsorted.sort()
     return unsorted[size-2]
   


num=[8,3,5]
unsorted=[12,45,30,18,40]
print( "all even product pairs:",pair_with_even_sum(num))
print("second sorted element in unsorted list :",second_largest_unsorted(unsorted))

 # for local checks
 
print( "all even product pairs:",pair_with_even_sum([1,3,5]))
print("second sorted element in unsorted list :",second_largest_unsorted([10,20,30,40,50,15]))