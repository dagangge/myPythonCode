#import random
#import time
#darts=1000*10000
#hits=0.0
#start=time.perf_counter()
#for i in range(1,darts+1):
#    x,y=random.random(),random.random()
#    dist=pow(x**2+y**2,0.5)
#    if dist<=1.0:
#        hits+=1
#pi=4*(hits/darts)

#print("圆周率值是：'{0}'".format(pi))
#print("运行时间是：'{0}'".format(time.perf_counter()-start))

import random
import time
darts=eval(input())
hits=0.0
start=time.perf_counter()
for i in range(1,darts+1):
    x,y=random.random(),random.random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits+=1
pi=4*(hits/darts)
print("{0:.6f}".format(pi))