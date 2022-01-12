import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/efesabanoglu/Downloads/cmpe48a-project-ecce664060c5.json'
from google.cloud import bigquery

bq_client = bigquery.Client()
table = bq_client.get_table("{}.{}.{}".format('cmpe48a-project', 'product_ds', 'products'))

if __name__ == '__main__':
    rows_to_insert = [{u"product_name": "Iphone 11",
                       u"photo": "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone11-green-select-2019_GEO_EMEA?wid=940&hei=1112&fmt=png-alpha&.v=1567021766404",
                       u"count": 1, u"price": 9999.99, u'is_in_the_basket':False},
                      {u"product_name": "Nike Air Force 1",
                       u"photo": "https://static.nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/b5d26789-8695-4ea4-80e0-47e59b6a3d8e/air-force-1-ayakkab%C4%B1s%C4%B1-vbt2HD.png",
                       u"count": 2, u"price": 1249.99, u'is_in_the_basket': False}
                      ]

    errors = bq_client.insert_rows_json(table, rows_to_insert)