import math
import numpy as np
j=7
i=0
D=0
m=[0 for indicator in range(10)]
d=[0 for indicator in range(25)]
Hin=0
Max=0
Sum=0
key_m=np.array([[1, 0, 0, 1/2, 1/2, 0, 1/3],
                [0, 1, 0, 1/2, 0, 1/2, 1/3],
                [0, 0, 1, 0, 1/2, 1/2, 1/3],
                [1/2, 1/2, 0, 1, 1/3, 1/3, 2/3],
                [1/2, 0, 1/2, 1/3, 1, 1/3, 2/3],
                [0, 1/2, 1/2, 1/3, 1/3, 1, 2/3],
                [1/3, 1/3, 1/3, 2/3, 2/3, 2/3, 1]])
def judge_none(a,b):
    if(a==0 and b==0):
        return 0
    if(a!=0 and b!=0):
        return 1
    else:
        return 2
def judge_weight_1(i,j):
   if(key_m[i,j]==0 and j<3):
       return math.exp(0)
   if(key_m[i,j]==0 and 3<=j<6):
       return math.exp(0)
   if(key_m[i,j]==1/2):
       return math.exp(1/2)
   if(key_m[i,j]==1/3):
       return math.exp(1/3)
   if(key_m[i,j]==2/3):
       return math.exp(2/3)
def judge_weight(i,j):
    h=0
    l=1
    sum=0
    while(h<6):
        while(l<7):
            sum=sum+judge_weight_1(h,l)
            l=l+1
        h=h+1
        l=h+1
    return sum/judge_weight_1(i,j)
def JS_divergence(q1,q2,i,k):
    if (judge_none(q1, q2) == 0):
        return 0
    if (judge_none(q1, q2) == 2):
        x1=math.log(max(q1,q2)/((q1+q2)/2),2)
        return judge_weight(i,k)*max(q1, q2) *math.exp(0) * x1/2
    else:
        x1=q1 * math.log(2*q1/(q1+q2), 2)
        x2=q2 * math.log(2*q2/(q1 + q2), 2)
        return (judge_weight(i, k) * (x1 + x2)/2)
while(i<j):
    m[i]=(float)(input())
    i=i+1
k=1
i=0
dnum=0
while(i<j):
    while(k<j):
        d[dnum]=round(JS_divergence(m[i],m[k],i,k),4)
        if(d[dnum]==0):
            print(0)
        else:
            print(d[dnum])
        Sum=Sum+d[dnum]
        k=k+1
    i=i+1
    k=i+1
i=0
Sum=math.log(Sum)

print('Sum:',round(Sum,4))













