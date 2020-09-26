dic={}
allcha=0
with open('7第七周文件和数据格式化\latex.log', 'r', encoding='utf-8') as f:
    for item in f:
        dic[item]=dic.get(item,0)+1
allline=set(dic)
print("共{}独特行".format(allcha))