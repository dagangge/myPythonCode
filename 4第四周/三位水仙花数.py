#result=""
#for x in range(100,1000):
#    if (pow(eval(str(x)[0]),3)+pow(eval(str(x)[1]),3)+pow(eval(str(x)[2]),3))==x:
#        result+=str(x)+","
#print(result[:-1])
result=[]
for x in range(100,1000):
    if (pow(eval(str(x)[0]),3)+pow(eval(str(x)[1]),3)+pow(eval(str(x)[2]),3))==x:
        result.append(str(x))
print("{}".format(','.join(result)))