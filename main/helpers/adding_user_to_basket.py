import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/bugra/Downloads/cmpe48a-project-434fa4ee5f87.json'
from google.cloud import bigquery

bq_client = bigquery.Client()
table = bq_client.get_table("{}.{}.{}".format('cmpe48a-project', 'basket_ds', 'baskets'))

if __name__ == '__main__':
    rows_to_insert = [{u"product_name": [],
                       u"user_name":"Bugra"}
                      ]

    errors = bq_client.insert_rows_json(table, rows_to_insert)