import csv
import uuid
import random

from faker import Faker


fake = Faker()

with open('outfile.csv', 'w') as outfile:
    orderwriter = csv.writer(outfile, delimiter='|') 

# 1. Create dict of items with:
# item_id, item_name, item_sku, item_manufactuerer, item_price, item_tax, item_total

# NO ANIMIALS WERE HARMED CREATING THIS CLOTHING
first_words = [
    'PenguinPolar',
    'Glacier',
    'Iceeeey',
    'Artic',
    'S-Pole Style',
    'Terran',
    'Ice Shelf',
    'Husky'
]

second_words = [
    'Sled',
    'Parka',
    'Crampon',
    'Carabiner',
    'Snowshoes',
    'Sunglasses',
    'Ice Pick',
    'Fishing Rod'
]

third_words = [
    'Blue',
    'Red',
    'Green',
    'Orange',
    'Purple',
    'Grey',
    'Teel',
    'Maroon',
    'Black'
]

product_names = set()

def random_product():
    return (
        random.choice(first_words) + ' ' + 
        random.choice(second_words) + ' - ' +
        random.choice(third_words)
    )

i=0
while i < 100000:
    i = i+1
    product_names.add(random_product())

product_data = {}

for i in product_names:
    product_data['item_id'] = str(uuid.uuid4())
    product_data['item_name'] = i
    item_sku = 

if  in first_words

first_words = [
    'PenguinPolar',
    'Glacier',
    'Iceeeey',
    'Artic',
    'S-Pole Style',
    'Terran',
    'Ice Shelf',
    'Husky'
]
order_id = uuid.uuid4()


# order_id (uuid) - partition key
# item_sku (sku)
# item_manufacturer ()
# item_price \
# item_tax  (order_price * 1.08)
# item_total (order_price+tax)
# order_timestamp (unix epoch in milliseconds)


# Make sure that there are spikes in specific 


# Sum item_price group by order to find largest orders
# find most popular products
# Make sure that there are spikes in specific PRODUCTS 
