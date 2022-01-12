import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/efesabanoglu/Downloads/cmpe48a-project-ecce664060c5.json'
from google.cloud import bigquery

bq_client = bigquery.Client()
SOURCE_TABLE = "cmpe48a-project.product_ds.products"

if __name__ == '__main__':
    bq_client = bigquery.Client()
    product_name = 'Iphone 11'
    user_name = 'Efe'
    query_for_insertion = """
                            INSERT INTO basket_ds.baskets(user_name, product_name)
                            VALUES('{USER_NAME}','{PRODUCT_NAME}')
                            ;
                            """.format(PRODUCT_NAME=product_name, USER_NAME=user_name)
    query_job = bq_client.query(query_for_insertion)
    results = query_job.result()

