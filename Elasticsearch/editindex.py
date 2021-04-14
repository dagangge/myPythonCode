# -*- coding:utf-8 -*-
from elasticsearch import Elasticsearch, helpers
from tqdm import tqdm
import pandas as pd
import os

elasticindex = pd.read_excel(
    "D:\Source\myPythonCode\pandas\ElasticSearch索引和文档说明.xlsx", None
)
sheets = elasticindex.keys()
keys = list(sheets)
hospitalprops = {}
deviceprops = {}


# es=Elasticsearch({"host":"localhost","port":"9200"})
ESSERVERS = [{"host": "172.16.12.122", "port": 9200}]
es:Elasticsearch = Elasticsearch(hosts=ESSERVERS)
# es = Elasticsearch(['localhost'],port=9200)


def getprops(keyname):
    df: pd.DataFrame = elasticindex[keyname]
    props = {}

    if df.columns.__contains__("加fields"):
        for item in df.index.values:
            if df.iloc[item].加fields == "是":
                props[df.iloc[item].key] = {
                    "type": df.iloc[item].数据类型,
                    "fields": {"keyword": {"type": "keyword"}},
                }
            else:
                props[df.iloc[item].key] = {"type": df.iloc[item].数据类型}
                # if df.iloc[item].数据类型 == "date":
                #     props[df.iloc[item].key] = {
                #         "format": "yyyy-MM-dd HH:mm:ss",
                #         "type": df.iloc[item].数据类型,
                #     }
    else:
        for item in df.index.values:
            props[df.iloc[item].key] = {"type": df.iloc[item].数据类型}
            # if df.iloc[item].数据类型 == "date":
            #     props[df.iloc[item].key] = {
            #         "format": "yyyy-MM-dd HH:mm:ss",
            #         "type": df.iloc[item].数据类型,
            #     }

    return props


def createIndex(my_index, df: pd.DataFrame):
    """
    新建索引
    """
    try:
        props = getprops(my_index)

        if "device" in df.key.values:
            props["device"] = {"type": "object", "properties": getprops("gk_device")}
        if "hospital" in df.key.values:
            props["hospital"] = {
                "type": "object",
                "properties": getprops("gk_hospital"),
            }

        body = {
            "properties": props,
        }
        # es.indices.create(index=my_index, ignore=400, body=body)
        # es.indices.create(index=my_index, body=body)
        es.indices.put_mapping(index=my_index, body=body)
        print("修改索引%s成功！" % (my_index))
    except Exception as e:
        print(f"修改索引${my_index}失败！${e}")


def deleteIndex(my_index):
    """
    删除索引
    """
    if es.indices.exists(my_index):
        es.indices.delete(my_index)
        print("删除索引%s成功！" % (my_index))


if __name__ == "__main__":
    for df in keys:
        # if df == "gk_hospital" or df == "gk_device" or df =="gk_sa_config" or df =="gk_st_config":
        # gk_st_config
        # gk_st_data
        # if df == "gk_st_config" or df =="gk_st_data":
        if df == "gk_st_config":
        # if (
        #     df == "gk_ps_config"
        #     or df == "gk_ps_data"
        #     or df == "gk_eo_config"
        #     or df == "gk_eo_data"
        #     or df == "gk_fs_config"
        #     or df == "gk_fs_data"
        #     or df == "gk_sa_config"
        #     or df == "gk_sa_data"
        #     or df == "gk_ws_config"
        #     or df == "gk_ws_data"
        #     or df == "gk_st_config"
        #     or df == "gk_st_data"
        # ):
            # deleteIndex(df)
            createIndex(df, elasticindex[df])