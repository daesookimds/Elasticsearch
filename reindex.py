import pandas as pd
from elasticsearch import Elasticsearch, helpers

def bulk_index() :

    data = pd.read_csv('ssg.csv')
    document = data.to_dict("records")
    es = Elasticsearch(hosts="localhost:9200")
    helpers.bulk(es, document, index='ssg_item_lv1')


def index() :
    data = pd.read_csv('ssg.csv')
    data['ssg_price'] = data['ssg_price'].apply(lambda x : x.replace(",", ""))
    data['ssg_price'] = data['ssg_price'].astype(int)
    document = data.to_dict("records")
    settings = open('config/settings.json').read()
    es = Elasticsearch(hosts="localhost:9200")
    es.indices.create(index='ssg_item_lv1', body=settings)
    helpers.bulk(es, document, index='ssg_item_lv1')





