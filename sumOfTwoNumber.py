
def sumOfTwoNumbers(num, target):
    output=[]
    n=len(num)
    for i in range(n):
        for j in range(i+1,n):
            curr_sum=num[i]+num[j]
            if curr_sum==target:
                print("target sum :",num[i],num[j])
                output.append(num[i])
                output.append(num[j])
                return output
    return output

num=[1,2,4,5,6,7,8]
print(sumOfTwoNumbers(num,10))
