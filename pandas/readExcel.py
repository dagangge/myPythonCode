import pandas as pd
import os

elasticindex=pd.read_excel("D:\Source\myPythonCode\pandas\ElasticSearch索引和文档说明.xlsx",None)
sheets = elasticindex.keys()
keys=list(sheets)
hospitalindex=elasticindex[keys[0]]
hospitaldata=elasticindex[keys[1]]                                                    
# print(hospitalindex)
# print(hospitaldata.loc[hospitaldata['省']=='四川省',:])
# print(hospitaldata.loc[hospitaldata.provincename=='四川省',:])
# print(hospitaldata.provincename.value_counts())
# print(hospitaldata.cityname.value_counts())

