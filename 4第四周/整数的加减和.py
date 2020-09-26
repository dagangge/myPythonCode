summ=0
for x in range(1,967):
    if x%2==0:
        summ-=x
    else:
        summ+=x
print(summ)
