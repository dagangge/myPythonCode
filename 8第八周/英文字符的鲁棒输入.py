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
    if complex(instr)==complex(eval(instr)):
        print(eval(instr)**2)
except :
    print("输入有误")