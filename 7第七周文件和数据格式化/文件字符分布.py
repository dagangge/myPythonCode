dic={}
allcha=0
with open('7第七周文件和数据格式化\latex.log', 'r', encoding='utf-8') as f:
    for item in f:
        for cha in item:
            dic[cha]=dic.get(cha,0)+1
            allcha+=1
strcha=""
strlist=list(dic.items())
strlist.sort()
for i in range(26):
    strcha+=","+chr(ord('a')+i)+":"+str(dic[chr(ord('a')+i)])
print("共{}字符{}".format(allcha,strcha))
