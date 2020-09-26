import sys
print("RECLIMIT:{}, EXEPATH:{}, UNICODE:{}".format(sys.getrecursionlimit(),sys.executable, sys.maxunicode))

#from tabulate import tabulate
#data = [ ["北京理工大学", "985", 2000],
#         ["清华大学", "985", 3000],
#         ["大连理工大学", "985", 4000],
#         ["深圳大学", "211", 2000],
#         ["沈阳大学", "省本", 2000],
#    ]
#headers = []
#print(tabulate(data, headers, tablefmt="grid"))