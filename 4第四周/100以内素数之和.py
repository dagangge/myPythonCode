result=0
def isSushu(args):
    for x in range(2,args):
        if args%x==0:
            return False
    return True
for x in range(2,100):
    if (isSushu(x)):
        result+=x
print(result)
