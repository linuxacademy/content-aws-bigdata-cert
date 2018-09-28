import json
import boto3
import time
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

s3 = boto3.client('s3')
sts = boto3.client('sts')

ES_URL = "https://search-newtestdomain123123-l4vrx66k6h6zotjqtkg3cmw5xi.us-east-1.es.amazonaws.com/"
credentials = boto3.Session().get_credentials()

awsauth = AWS4Auth(
    credentials.access_key,
    credentials.secret_key, 
    'us-east-1',
    'es',
    session_token=credentials.token
)

es_client = Elasticsearch(
    hosts=[{'host': ES_URL, 'port': 443}], 
    http_auth=awsauth, 
    use_ssl=True, 
    verify_certs=True, 
    connection_class=RequestsHttpConnection
)

def record_order(doc):
    """Post an order to the ES Cluster index"""
    es_client.index(
        index="orders", 
        doc_type="order", 
        body=doc
    )

def lambda_handler(event, context):
    for record in event['Records']:
        es_doc = {}
        if record['eventName'] == 'INSERT':
            es_doc['item_id'] = record['dynamodb']['NewImage']['item_id']['S']
            es_doc['item_name'] = record['dynamodb']['NewImage']['item_name']['S']
            es_doc['item_total'] = record['dynamodb']['NewImage']['item_total']['S']
            es_doc['customer_name'] = record['dynamodb']['NewImage']['customer_name']['S']
        if ES_URL == "":
            print(es_doc)
        else: 
            print(es_doc)
            record_order(es_doc)
        time.sleep(1)
