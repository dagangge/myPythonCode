# encoding: utf-8 
import clr
#clr.AddReference()
#from WindowsFormsTest import Program
clr.FindAssembly("WindowsFormsTest.dll")
from WindowsFormsTest import *


def test():
    dd=Form1()
    dd.ShowDialog()
    print("被调用")

if __name__ == '__main__':
    test()
