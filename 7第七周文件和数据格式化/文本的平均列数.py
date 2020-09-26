allcha=0
allline=0
with open('7第七周文件和数据格式化\latex.log', 'r', encoding='utf-8') as f:
    for item in f:
        if len(item)<=0:
            continue
        allline+=1
        for cha in item:
            allcha+=1
colums=(allcha/allline)
print("{}".format(colums))