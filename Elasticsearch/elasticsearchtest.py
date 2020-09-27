from elasticsearch import Elasticsearch,helpers
from tqdm import tqdm

# es=Elasticsearch({"host":"localhost","port":"9200"})
ESSERVERS=[{
    "host":"localhost",
    "port":9200
}]
es = Elasticsearch(hosts=ESSERVERS)


def createIndex(my_index):
    """
    新建索引
    """    
    settings = {
        "mappings": {
            "properties": {
                "my_id": {"type": "integer"},
                "my_word": {"type": "text"}
                # "title": {"type": "text"},
                # "url": {"type": "text"},
                # "date": {"type": "date"}
            }
        }
    }
    es.indices.create(index=my_index,ignore=400, body=settings)
    print("创建索引%s成功！" %(my_index))


def deleteIndex(my_index):
    """
    删除索引
    """
    if es.indices.exists(my_index):
        es.indices.delete(my_index)
        print("删除索引%s成功！" %(my_index))

def getAllWords(path="Elasticsearch/threekingdoms.txt"):
    words=[]
    # i=0
    # with open(path,"r",encoding="utf-8") as f:
    #     for item in f:
    #         i+=1
    #         words.append((i,item.strip()))
   
    with open(path,"r",encoding="utf-8") as f:
        for i, item in enumerate(f.readlines()):
            words.append((i,item.strip()))
    return words

def insertData(words,myindex,onebulk):
    """
    批量插入数据
    #onebulk表示一个bulk里装多少个,即一次插入多少条
    """
    body = []
    body_count = 0  #记录body里面有多少个. 

    print("共需要插入%d条..."%len(words))
    pbar=tqdm(total=len(words))
    
    for id,word in words:
        data1={
            "my_id":id,
            "my_word":word
        }
        everybody={
            "_index":myindex,
            "_source":data1
        }
        if body_count<onebulk:
            body.append(everybody)
            body_count+=1
        else:
            helpers.bulk(es,body)
            pbar.update(onebulk)
            body_count=0
            body=[]
            body.append(everybody)
            body_count+=1
    #如果body里面还有，则再插入一次（最后非整块的）
    if len(body):
        helpers.bulk(es,body)
    pbar.close()
    #res = es.index(index=my_index,doc_type=my_doc,id=my_key_id,body=data1)  #一条插入
    print("插入数据完成")

def keywordSearch(keywords,myindex):
    """
    查询
    """
    mysearch={
        "query":{
            "match":{
                "my_word":keywords
            }
        }
    }
    # 直接查询
    # res=es.search(index=myindex,body=mysearch)
    # total=res["hits"]["total"]["value"]
    # print("共查询到 %d" %total)

    # helpers查询
    res=helpers.scan(
        client=es,
        query=mysearch,
        scroll='10m',#查询一次数据在ES中缓存10分钟再销毁
        index=myindex,
        timeout='10m'
    )
    print(res) #generator object scan at 0x0A686930    
    res=[item for item in res]
    # print(res) #generator object scan at 0x0A686930
    searchres=[]
    for item in res:
        tmp=item["_source"]
        searchres.append((tmp["my_id"],tmp["my_word"]))
    print("共查询到%d"%len(res))
    print(searchres)



if __name__ == "__main__":
    my_index = "news"
    # createIndex(my_index)
    # deleteIndex(my_index)
    # words=getAllWords()
    # insertData(words,my_index,onebulk=100)
    keywords="刘备张飞"
    keywordSearch(keywords,my_index)
