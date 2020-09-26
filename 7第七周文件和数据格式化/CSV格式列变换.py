dic={}
allcha=0
with open('7第七周文件和数据格式化\data.csv', 'r', encoding='utf-8') as f:
    for item in f:
        chalist= item.strip('\n').split(',')
        # str(chalist).join(',')
        for x in range(len(chalist)):
            if x==0:
                print("{}".format(chalist[-(x+1)]),end="")
            else:
                print(",{}".format(chalist[-(x+1)]),end="")
        print("\r")

dic={}
allcha=0
with open('7第七周文件和数据格式化\data.csv', 'r', encoding='utf-8') as f:
    for item in f:
        chalist= item.strip("\n").split(',')
        chalist=chalist[::-1]
        print(",".join(chalist))


# f = open("data.csv")
# for line in f:
#     line = line.strip("\n")
#     ls = line.split(",")
#     ls = ls[::-1]
#     print(",".join(ls))
# f.close()

dic={}
allcha=0
with open('7第七周文件和数据格式化\data.csv', 'r', encoding='utf-8') as f:
    lines=f.read()
    lines=lines[::-1]
    for line in lines:
        chalist= line.split(',')
        chalist=chalist[::-1]
        print(";".join(chalist))