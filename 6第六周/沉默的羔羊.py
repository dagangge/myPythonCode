#import jieba
#def function():
#    with open("6第六周\沉默的羔羊.txt","r",encoding="utf-8") as f:
#        txt=f.read()
#        return txt
#words=jieba.lcut(function())
#counts={}
#for x in words:
#    if len(x)>2:
#        counts[x]=counts.get(x,0)+1
#items=list(counts.items())
#items.sort(key=lambda x:x[1],reverse=True)
#for i in range(1):
#    word, count = items[i]
#    print ("{}".format(word))


import jieba
f = open("6第六周\沉默的羔羊.txt","r",encoding="utf-8")
ls = jieba.lcut(f.read())
#ls = f.read().split()
d = {}
for w in ls:
    d[w] = d.get(w, 0) + 1
maxc = 0
maxw = ""
for k in d:
    if d[k] > maxc and len(k) > 2:
        maxc = d[k]
        maxw = k
    if d[k] == maxc and len(k) > 2 and k > maxw:
        maxw = k
print(maxw)
f.close()