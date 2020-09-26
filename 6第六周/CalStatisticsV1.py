##CalStatisticsV1.py
#def getNum():       #获取用户不定长度的输入
#    nums = []
#    iNumStr = input("请输入数字(回车退出): ")
#    while iNumStr != "":
#        nums.append(eval(iNumStr))
#        iNumStr = input("请输入数字(回车退出): ")
#    return nums

#def mean(numbers):  #计算平均值
#    s = 0.0
#    for x in numbers:
#        s+=x
#    return s / len(numbers)

#def dev(numbers, mean): #计算方差
#    sdev = 0.0
#    for num in numbers:
#        sdev = sdev + (num - mean)**2
#    return pow(sdev / (len(numbers)-1), 0.5)

#def median(numbers):    #计算中位数
#    sorted(numbers)
#    size = len(numbers)
#    if size % 2 == 0:
#        med = (numbers[size//2-1] + numbers[size//2])/2
#    else:
#        med = numbers[size//2]
#    return med

#n =  getNum() #主体函数
#m =  mean(n)
#print("平均值:{},方差:{:.2},中位数:{}.".format(m, dev(n,m),median(n)))

#请在...补充一行或多行代码
#CalStatisticsV1.py
def getNum():       #获取用户不定长度的输入
    iNumStr=input()
    nums=list(eval(iNumStr))
    return nums

def mean(numbers):  #计算平均值
    su=0
    for x in numbers:
        su+=x
    return su / len(numbers)
    
def dev(numbers, mean): #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)

def median(numbers):    #计算中位数
    numbers= sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[size//2]
    return med
    
n =  getNum() #主体函数
m =  mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m,dev(n,m),median(n)))