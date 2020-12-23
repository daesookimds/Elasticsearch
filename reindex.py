import pandas as pd
from elasticsearch import Elasticsearch, helpers

def bulk_index() :

    data = pd.read_csv('ssg.csv')
    document = data.to_dict("records")
    es = Elasticsearch(hosts="localhost:9200")
    helpers.bulk(es, document, index='ssg_item_lv1')





