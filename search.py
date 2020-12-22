from elasticsearch import Elasticsearch

def match_all(keyword) :
    '''
    모든 문서와 매치
    '''
    es = Elasticsearch('localhost:9200')
    search_result = es.search(
        index="ssg_item",
        body={
            "query": {
                "match_all": {
                    "query": keyword
                }
            }
        }
    )
