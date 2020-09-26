#CalHamletV1.py
def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt
    
def function():
    with open("6第六周\hamlet.txt","r") as f:
        txt=f.read()
        txt= txt.lower()
        for x in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
            txt=txt.replace(x," ")
        return txt

hamletTxt = function()
words  = hamletTxt.split()
counts = {}
for word in words:			
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
input()




