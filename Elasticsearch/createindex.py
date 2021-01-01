from elasticsearch import Elasticsearch, helpers
from tqdm import tqdm
import pandas as pd
import os

elasticindex = pd.read_excel(
    "D:\Source\myPythonCode\pandas\ElasticSearch索引和文档说明.xlsx", None)
sheets = elasticindex.keys()
keys = list(sheets)
hospitalprops={}
deviceprops={}


# es=Elasticsearch({"host":"localhost","port":"9200"})
ESSERVERS = [{
    "host": "localhost",
    "port": 9200
}]
es = Elasticsearch(hosts=ESSERVERS)


def createIndex(my_index, df: pd.DataFrame):
    """
    新建索引
    """
    try:
        props = {}
       
        if df.columns.__contains__("加fields"):
            for item in df.index.values:
                if df.iloc[item].加fields == "是":
                    props[df.iloc[item].key] = {
                        "type": df.iloc[item].数据类型,
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    }
                else:
                    if df.iloc[item].key=="device":
                        props[df.iloc[item].key] = deviceprops
                    elif df.iloc[item].key=="hospital":
                        props[df.iloc[item].key] = hospitalprops                    
                    else:
                        props[df.iloc[item].key] = {
                        "type": df.iloc[item].数据类型
                    }
        else:
            for item in df.index.values:
                if df.iloc[item].key=="device":
                    props[df.iloc[item].key] = deviceprops
                elif df.iloc[item].key=="hospital":
                    props[df.iloc[item].key] = hospitalprops                    
                else:
                    props[df.iloc[item].key] = {
                    "type": df.iloc[item].数据类型
                }
        if my_index=="gk_hospital":
            hospitalprops=props
        if my_index=="gk_device":
            deviceprops=props

        settings = {
            "mappings": {
                "properties": props
            }
        }
        es.indices.create(index=my_index, ignore=400, body=settings)
        print("创建索引%s成功！" % (my_index))
    except:
        print("创建索引%s失败！"% (my_index))
    


def deleteIndex(my_index):
    """
    删除索引
    """
    if es.indices.exists(my_index):
        es.indices.delete(my_index)
        print("删除索引%s成功！" % (my_index))


if __name__ == "__main__":
    # my_index = keys[0]
    for df in keys:
        deleteIndex(df)
        createIndex(df, elasticindex[df])   
    
    # words=getAllWords()
    # insertData(words,my_index,onebulk=100)
    # keywords = "刘备张飞"
    # keywordSearch(keywords, my_index)
