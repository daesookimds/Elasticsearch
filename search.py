from elasticsearch import Elasticsearch

def match_all() :
    '''
    모든 문서내 검색
    '''
    es = Elasticsearch('localhost:9200')
    search_result = es.search(
        index="ssg_item_lv1",
        body={
            "query": {
                "match_all": {}
            }
        }
    )

    return search_result

def match(keyword) :
    '''
    지정한 필드의 전문 검색
    '''
    es = Elasticsearch('localhost:9200')
    search_result = es.search(
        index="ssg_item_lv1",
        body={
            "query": {
                "match": {
                    "item_nm": keyword
                }
            }
        }
    )

    return search_result


def dix_max(keyword) :
    '''
    가장 정확한 문서 매치 검색
    '''
    es = Elasticsearch('localhost:9200')
    search_result = es.search(
        index="ssg_item_lv1",
        body={
            "query": {
                "dis_max": {
                    "queries": [
                        {"match": {"item_nm" : keyword}},
                        {"match": {"cat_nm": keyword}}
                    ]
                }
            }
        }
    )

    return search_result

def multi_match(keyword) :
    '''
    tpye에 따라 문서 검색 점수 반영
    - best_fields : dis_max와 같은 동작 (정확하게 매치된 문서)
    - most_fields : 매치되는 필드가 많은 문서에 높은 점수
    - cross_fields : 모든 필드를 하나에 필드로 합친 것처럼 검색
    '''
    es = Elasticsearch('localhost:9200')
    search_result = es.search(
        index="ssg_item_lv1",
        body={
            "query": {
                "multi_match": {
                    "query": keyword,
                    "fields": ['item_nm', 'cat_nm'],
                    "tie_breaker": 0.2,
                    "type": "most_fields"
                }
            }
        }
    )

    return search_result

