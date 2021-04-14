from elasticsearch_dsl import connections,Search,Q,query
from tqdm import tqdm

connections.create_connection(hosts=[{"host":"172.16.12.122","port":9200}],timeout=20)


def keywordSearch(keywords, myindex):
    """
    查询
    """    
    s=Search(index=myindex).query("match",hospitalid=keywords)
    res=s.execute()
    print(res.success())
    print(res.took)    
    print(res.hits.total.value)
    print(res.hits.total.relation)
    print(res.to_dict())
    print(res.hits)
    print(res.hits.max_score)
    h= res.hits[0]
    print(h.meta)

    for item in res.hits:
        print(item)
        print(item.hospitalid)
        print(item.hospitalname)
    
# True
# 1
# 1
# eq
# {'took': 1, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1, 'relation': 'eq'}, 'max_score': 5.028257, 'hits': [{'_index': 'gk_hospital', '_type': '_doc', '_id': '0mng3HcBxFmq_60p8lU5', '_score': 5.028257, '_source': {'hospitalid': 'HS102847', 'hospitalname': '淄博市中心医院西院', 'provinceid': 11.0, 'provincename': '山东省', 'cityid': 85.0, 'cityname': '淄博市', 'levelname': '三甲', 'xy': '118.05928600167,36.8137249323249', 'createdate': '2021-02-26T13:47:36.431575'}}]}}
# [<Hit(gk_hospital/0mng3HcBxFmq_60p8lU5): {'hospitalid': 'HS102847', 'hospitalname': '淄博市中心医院西院', 'pro...}>]
# 5.028257
# {'index': 'gk_hospital', 'id': '0mng3HcBxFmq_60p8lU5', 'scor...}
# <Hit(gk_hospital/0mng3HcBxFmq_60p8lU5): {'hospitalid': 'HS102847', 'hospitalname': '淄博市中心医院西院', 'pro...}>
# HS102847
# 淄博市中心医院西院


if __name__ == "__main__":
    my_index = "gk_hospital"
    # keywords = "山东省"
    keywords = "HS102847"
    keywordSearch(keywords, my_index)
