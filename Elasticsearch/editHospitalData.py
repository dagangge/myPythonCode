# -*- coding:utf-8 -*-
from elasticsearch import Elasticsearch, helpers
from tqdm import tqdm
import pandas as pd
import os, datetime, math

elasticindex = pd.read_excel(
    "D:\Source\myPythonCode\pandas\ElasticSearch索引和文档说明.xlsx", None
)
sheets = elasticindex.keys()
keys = list(sheets)
hospitalprops = {}
deviceprops = {}


# es=Elasticsearch({"host":"localhost","port":"9200"})
ESSERVERS = [{"host": "172.16.12.122", "port": 9200}]
es = Elasticsearch(hosts=ESSERVERS)
# es = Elasticsearch(['localhost'],port=9200)


def gethospitalList():
    df: pd.DataFrame = elasticindex["医院数据"]
    datalist = []

    for item in df.index.values:
        if df.iloc[item].hospitalid:
            props = {}
            for col in list(df.columns):
                if not col.__contains__("Unnamed"):
                    if not pd.isna(df.iloc[item][col]):
                        props[col] = df.iloc[item][col]
            props["createdate"] = datetime.datetime.now()
            datalist.append(props)
    return datalist


def insertData(my_index, df: pd.DataFrame):
    """
    新建索引
    """
    try:
        # for hos in gethospitalList():
        #     es.index(index=my_index, doc_type="_doc", body=hos)
        hos = {
            # 'script': "ctx._source. = '32325444'"
            "doc": {"hospitalname": "888888", "hospitalid": "888888"}
        }

        exist = es.exists(index=my_index, id="12ng3HcBxFmq_60pylGU")
        if exist:
            es.update(
                index=my_index, id="12ng3HcBxFmq_60pylGU", doc_type="_doc", body=hos
            )
        else:
            hos = {
                "hospitalname": "666666", 
                "hospitalid": "666666"
            }
            es.index(index=my_index, doc_type="_doc", body=hos)

        print("插入数据%s成功！" % (my_index))
    except Exception as e:
        print(f"添加数据${my_index}失败！${e}")


if __name__ == "__main__":
    # my_index = keys[0]
    for df in keys:
        if df == "gk_hospital":
            insertData(df, elasticindex[df])

    # words=getAllWords()
    # insertData(words,my_index,onebulk=100)
    # keywords = "刘备张飞"
    # keywordSearch(keywords, my_index)
