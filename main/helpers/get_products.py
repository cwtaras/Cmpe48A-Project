import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/efesabanoglu/Downloads/cmpe48a-project-ecce664060c5.json'
from google.cloud import bigquery

bq_client = bigquery.Client()
SOURCE_TABLE = "cmpe48a-project.product_ds.products"

if __name__ == '__main__':
    products = {}
    bq_client = bigquery.Client()
    product_names = ['Nike Air Force 1', 'Iphone 11']
    for product in product_names:
        query_for_specifics = """
                    SELECT *
                    FROM `cmpe48a-project.product_ds.products`
                    WHERE product_name = '{PRODUCT_NAME}';
                    """.format(PRODUCT_NAME=product)
        query_job = bq_client.query(query_for_specifics)
        results = query_job.result()
        for row in results:
            product = {'photo': row.photo, 'count': row.count,
                       'price': row.price, 'is_in_the_basket': row.is_in_the_basket}
            products[row.product_name] = product
    print(products)