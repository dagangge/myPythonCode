#import re
#instr=input()
#outstr=list()
#try:
#    for x in instr:
#        if re.match("[a-zA-Z]",x):
#            outstr.append(x)
#    string="".join(outstr)
#    print(string)
#except :
#    #pass

import re
instr=input()
try:
    instr=instr.replace(" ","")
    print(instr)        
except :
    print("输入有误")