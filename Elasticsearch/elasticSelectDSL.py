from elasticsearch_dsl import connections,Search,Q
from tqdm import tqdm

connections.create_connection(hosts=[{"host":"172.16.12.122","port":9200}],timeout=20)


def keywordSearch(keywords:dict, myindex):
    """
    查询
    """
    must=[]
    for item in keywords.items():
        must.append(Q("match",**{item[0]:item[1]}))
    # s=Search(index=myindex).query("match",**keywords)
    if len(must)>1:
        s=Search(index=myindex)
        s.query=Q('bool',must=must)
        res=s.execute()
        print(res.success())
        print(res.took)    
        print(res.hits.total.value)
        print(res.hits.total.relation)
        print(res.to_dict())
        print(res.hits)
        print(res.hits.max_score)

        for item in res.hits:
            print(item)
            print(item.to_dict())
            print(item.meta)
            print(item.id)
            print(item.name)
    elif len(must)==1:
        s=Search(index=myindex).query(must[0])
        res=s.execute()
        print(res.success())
        print(res.took)    
        print(res.hits.total.value)
        print(res.hits.total.relation)
        print(res.to_dict())
        print(res.hits)
        print(res.hits.max_score)
    
# True
# 2
# 1
# eq
# {'took': 2, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1, 'relation': 'eq'}, 'max_score': 3.7786646, 'hits': [{'_index': 'gk_device', '_type': '_doc', '_id': 'lW1pEHgBxFmq_60pe3Bc', '_score': 3.7786646, '_source': {'id': 'DCPM01', 'ip': '10.1.100.223', 'name': '1#能源监控2.0', 'no': 1, 'type': 'PM', 'subtype': 2.0, 'totalno': 58, 'port': 7002, 'volume': 1000, 'doors': 2, 'workmode': 3, 'isconnect': 1, 'sterimode': 4, 'isshow': 1, 'isslave': 1, 'protocoltype': 2, 'printtype': 2, 'deleteflag': 0, 'ordernumber': '15', 'volumeratio': 90, 'hospital': {'hospitalid': 'HS102831', 'createdate': '2021-03-08T13:57:30.915184', 'hospitalname': '淄博市妇幼保健院
# 新院', 'provinceid': 11.0, 'provincename': '山东省', 'cityid': 85.0, 'cityname': '淄博市', 'levelname': '三甲', 'xy': '118.083006297644,36.9588579972321'}}}]}}
# [<Hit(gk_device/lW1pEHgBxFmq_60pe3Bc): {'id': 'DCPM01', 'ip': '10.1.100.223', 'name': '1#能源监控2.0', ...}>]
# 3.7786646
# <Hit(gk_device/lW1pEHgBxFmq_60pe3Bc): {'id': 'DCPM01', 'ip': '10.1.100.223', 'name': '1#能源监控2.0', ...}>
# {'index': 'gk_device', 'id': 'lW1pEHgBxFmq_60pe3Bc', 'score'...}
# DCPM01
# 1#能源监控2.0


if __name__ == "__main__":
    my_index = "gk_device"
    keywords={"hospital.hospitalid":"HS102831"}
    # keywords={"id":"DCPM01","hospital.hospitalid":"HS102831"}
    keywordSearch(keywords, my_index)
