import time

import numpy as np
from matplotlib import pyplot as plt

epoch = 1000
t=time.time()
n=1000000
prob=np.zeros((50,1))
for x1 in range (epoch):
    a=np.ones((n,1))
    a[0][0]=0
    flag=1
    t2=1
    while flag:
        t2 += 1
        t1=int(n-np.sum(a,axis=0))
        b=np.random.randint(0,n,(t1,1))
        for x in range(t1):
            a[b[x][0]][0]=0
        if np.argmax(a)== 0:
            flag = 0
    prob[t2][0] +=1
prob=prob/epoch
print(prob)
y=[]
for x in range (50):
    y.append(x+1)
plt.bar(y,prob.tolist())
plt.xlabel('number of days')
plt.ylabel('probability')
plt.title('probability distribution of number of days taken for n = 1000000')
plt.savefig('1.png')
plt.show()
print(time.time()-t)