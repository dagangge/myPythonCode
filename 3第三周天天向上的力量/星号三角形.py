def printN(n,N):
    if n==1:
        xing="*"
    elif n==2:
        xing="*"
    else:
        xing="*"*n
    print("{:^{}}".format(xing,N))
inputV=input()
total=eval(inputV)
for x in range(1,eval(inputV)+1,2):
    printN(x,total)


    n = eval(input())
for i in range(1,n+1,2):
    print("{0:^{1}}".format('*'*i, n))