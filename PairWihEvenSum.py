

def pairWithEvenSum(num):
    pair_output=[]
    n=len(num)
    for i in range(n):
        for j in range(1+i,n):
            product=num[i]*num[j]
            if product%2==0:
                print("even product found :" ,num[i],num[j])
                pair_output.append(num[i],num[j])
                return pair_outputnum = [8,9,3,4,1,2]
            print(pairWithEvenSum(num))