import time
scale=50
print("开始".center(scale//2,"-"))
start=time.perf_counter()
for x in range(scale+1):
    a='*'*x
    b='.'*(scale-x)
    c=(x/scale)*100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n结束".center(scale//2,'-'))
