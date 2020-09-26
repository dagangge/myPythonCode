TempStr = input()
if '+' in TempStr:
    index=TempStr.index('+')
    result= eval(TempStr[0:index])+eval(TempStr[index+1:])
    print("{:.2f}".format(result))
elif ('-' in TempStr) and TempStr.index('-')>0:
    index=TempStr.index('-')
    result= eval(TempStr[0:index])-eval(TempStr[index+1:])
    print("{:.2f}".format(result))
elif '*' in TempStr:
    index=TempStr.index('*')
    result= eval(TempStr[0:index])*eval(TempStr[index+1:])
    print("{:.2f}".format(result))
elif '/' in TempStr:
    index=TempStr.index('/')
    result= eval(TempStr[0:index])/eval(TempStr[index+1:])
    print("{:.2f}".format(result))
