n = input()
li=list()
for x in n:
    li.append(x)
sets=set(li)
summ=0
for x in sets:
    summ+=int(x)
print(summ)
