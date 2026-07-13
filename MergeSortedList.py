
a=[2,4,5,6,7,8,8,8]
b=[1,6,7,12,30]
merge=[]
i=0
j=0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        merge.append(a[i])
        i=i+1
    else:
        merge.append(b[j])
        j=j+1

while i<len(a):
    merge.append(a[i])
    i=i+1
while j<len(b):
    merge.append(b[j]) 
    j=j+1
print( "merged List: ",merge)
