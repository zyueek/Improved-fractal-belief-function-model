import math
import numpy as np
j=7
m1=[0 for indicator in range(10)]
m2=[0 for indicator in range(10)]
d=[0 for indicator in range(25)]
collision_rate=0
sum1=0
i=0
key_m=np.array([[1, 0, 0, 1/2, 1/2, 0, 1/3],
                [0, 1, 0, 1/2, 0, 1/2, 1/3],
                [0, 0, 1, 0, 1/2, 1/2, 1/3],
                [1/2, 1/2, 0, 1, 1/3, 1/3, 2/3],
                [1/2, 0, 1/2, 1/3, 1, 1/3, 2/3],
                [0, 1/2, 1/2, 1/3, 1/3, 1, 2/3],
                [1/3, 1/3, 1/3, 2/3, 2/3, 2/3, 1]])
print("input the num of m1")
while(i<j):
    m1[i]=(float)(input())
    i=i+1
i=0
print("input the num of m2")
while(i<j):
    m2[i]=(float)(input())
    i=i+1
i=0
k=0
while(i<7):
    while(k<7):
        if(key_m[i][k]==0):
            sum1=m1[i]*m2[k]+sum1
        k=k+1
    collision_rate = sum1 + collision_rate
    k=0
    i=i+1
    sum1=0
collision_rate=round(1-collision_rate,4)
print("k=",collision_rate)
i=0
k=0
sum1=0
sum2=0
sum3=0
while(i<7):
    while(k<7):
        if(key_m[i][k]==1 and i<3):
            sum1=m1[i]*m2[k]+sum1
        if (0<key_m[i][k]<1 and i < 3):
            sum1 = m1[i] * m2[k]+m1[k]*m2[i]+ sum1
        if (key_m[i][k] == 2/3 and 3 <= i < 6):
            sum2 = m1[i] * m2[k]+m1[k]*m2[i]+ sum2
        if (key_m[i][k] == 1 and 3 <= i < 6):
            sum2 = m1[i] * m2[k] + sum2
        if(key_m[i][k] ==1 and i==6):
            sum3 = m1[i] * m2[k] + sum3
        k=k+1
    outcome=(1/collision_rate)*max(sum1,sum2,sum3)
    print(round(outcome,2))
    sum1=0
    sum2=0
    sum3=0
    k=0
    i=i+1


