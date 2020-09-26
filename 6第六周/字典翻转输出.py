strin=input()
try:
    strdir=eval(strin)
    print(type(strdir))
    newdir={}
    for x in strdir:
        newdir[strdir[x]]=x
    print(str(newdir))
except :
    print("输入错误")
