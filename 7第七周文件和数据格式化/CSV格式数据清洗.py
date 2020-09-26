dic={}
allcha=0
with open('7第七周文件和数据格式化\data.csv', 'r', encoding='utf-8') as f:
    for item in f:
        chalist= str(item).replace(' ','').split(',')
        print(",".join(chalist))
with open('data.csv') as f:
    item=f.read()
    item=item.replace(" ","")
    print(item)
        