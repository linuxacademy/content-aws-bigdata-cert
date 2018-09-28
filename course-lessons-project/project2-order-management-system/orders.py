import boto3
import csv
import uuid
import random
import time
from collections import Counter

from faker import Faker

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PenguinOrders')
fake = Faker()

# NO ANIMIALS WERE HARMED CREATING THIS CLOTHING
manufacturers = [
    ['PenguinPolar', 1.8],
    ['Glacier', 1.3],
    ['Iceeeey', 0.6],
    ['Artic', 0.89],
    ['S-PoleStyle', 0.7],
    ['Terran', 0.8],
    ['IceShelf', 1.0],
    ['Husky', 1.1],
]

items = [
    ['Sled', 70],
    ['Parka', 20],
    ['Crampon', 135],
    ['Carabiner', 3],
    ['Snowshoes', 235],
    ['Sunglasses', 30],
    ['Ice Pick', 85],
    ['Fishing Rod', 189]
]

order_ids = []
num_ids = 0
# 2000 possible orders to group the items into
while num_ids < 2000:
    order_ids.append(str(uuid.uuid4()))
    num_ids = num_ids + 1

def create_order_data():
    manufacturer = random.choice(manufacturers)
    item = random.choice(items)
    order = {}
    order['order_id'] = random.choice(order_ids)
    order['item_id'] = str(uuid.uuid4())
    order['item_name'] = manufacturer[0] + ' ' + item[0]
    order['item_type'] = item[0]
    order['item_sku'] = order['item_name'][0:4].upper().replace('-','')
    order['color'] = fake.color_name()
    order['item_price'] = str(round(manufacturer[1] * item[1])+.99)
    order['item_tax'] = str(round((float(order['item_price']) * .03), 2))
    order['item_total'] = str(float(order['item_price']) + float(order['item_tax']))
    order['item_manufacturer'] = manufacturer[0]
    order['customer_name'] = fake.name()
    order['customer_phone_number'] = fake.phone_number()
    return order

def send_to_dynamodb(item):
    print('Sending item to DynamoDB: ' + str(item))
    table.put_item(Item=item)

def write_orders():
    n = 0
    while n < 100000:
        time.sleep(.25)
        n = n + 1
        # Create random order
        new_order = create_order_data()
        # When true, used to occassionally throw 
        # out things that aren't PenguinPolar
        condition1 = [
            new_order['item_manufacturer'] != 'PenguinPolar', 
            random.randint(1,101) > 70
        ]
        # When true, used to occassionally throw out 
        # things that aren't Sunglasses or Carabiners
        condition2 = [
            new_order['item_type'] not in ['Sunglasses','Carabiner'],
            random.randint(1,101) > 70
        ]
        # When true, used to occassionally throw out 
        # Ice Pick and Crampons
        condition3 = [
            new_order['item_type'] in ['Ice Pick','Crampon'],
            random.randint(1,101) > 20
        ]
        if all(condition1) or all(condition2) or all(condition3):
            new_order = create_order_data()
            send_to_dynamodb(new_order)
        else:
            send_to_dynamodb(new_order)
        
if __name__ == '__main__':
    write_orders()