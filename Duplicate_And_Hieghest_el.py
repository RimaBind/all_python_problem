
list=[12,4,5,6,6,12,7,8,9,3,4,5,67,78,29]
max=list[0]
for score in list:
    if score>max:
        max=score


dup=[]
count={}
for num in list:
    count[num]=count.get(num,0)+1

for k,v in count.items():
    if v>1:
        dup.append(k)    

print("Scores :",list)   
print("Hieghest :",max) 
print("Dupplicates Elements :",dup)