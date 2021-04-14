from elasticsearch import Elasticsearch, helpers
from tqdm import tqdm

# es=Elasticsearch({"host":"localhost","port":"9200"})
ESSERVERS = [
    {
        # "host":"localhost",
        "host": "172.16.12.122",
        "port": 9200,
    }
]
es = Elasticsearch(hosts=ESSERVERS)


def keywordSearch(keywords, myindex):
    """
    查询
    """
    mysearch = {
        "query": {
            "match_all":{},
            # "constant_score":{"filter": {"term": {"cityid": keywords}}}
        },
        "size": 10000,
    }
    # 直接查询
    # res=es.search(index=myindex,body=mysearch)
    # print(res)
    # total=res["hits"]["total"]["value"]
    # resc=[item for item in res["hits"]["hits"]]
    # # print(res) #generator object scan at 0x0A686930
    # searchres=[]
    # for item in resc:
    #     tmp=item["_source"]
    #     searchres.append((tmp["hospitalid"],tmp["hospitalname"]))
    # print("共查询到 %d" %total)
    # print(f"查询结果 {searchres}{len(searchres)}")

    # helpers查询
    res = helpers.scan(
        client=es,
        query=mysearch,
        scroll="5m",  # 查询一次数据在ES中缓存10分钟再销毁
        index=myindex,
        timeout="10m",
    )
    print(res)  # generator object scan at 0x0A686930
    res = [item for item in res]
    # print(res) #generator object scan at 0x0A686930
    searchres = []
    for item in res:
        tmp = item["_source"]
        searchres.append((tmp["hospitalid"], tmp["hospitalname"]))
    print("共查询到%d" % len(res))
    print(searchres)


if __name__ == "__main__":
    my_index = "gk_hospital"
    # keywords = "山东省"
    keywords = "292"
    keywordSearch(keywords, my_index)
