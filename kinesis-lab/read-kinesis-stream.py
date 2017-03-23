import boto3
import json
from datetime import datetime
import time

stream_name = 'delivery-1'

kinesis_client = boto3.client('kinesis', region_name='us-east-1')

## describe_stream to get the shard
response = kinesis_client.describe_stream(StreamName=stream_name)
shard_id = response['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = kinesis_client.get_shard_iterator(
    StreamName=stream_name,
    ShardId=shard_id,
    ShardIteratorType='TRIM_HORIZON'
)

my_shard_iterator = shard_iterator['ShardIterator']

record_response = kinesis_client.get_records(
    ShardIterator=my_shard_iterator,
    Limit=1
)
print record_response['Records'][0]['Data']

while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(
        ShardIterator=record_response['NextShardIterator'],
        Limit=1
    )

    print record_response['Records'][0]['Data']


    time.sleep(1)
