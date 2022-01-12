import ast
import json
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/efesabanoglu/Downloads/cmpe48a-project-ecce664060c5.json'
from google.cloud import bigquery
import requests

SOURCE_TABLE = "cmpe48a-project.product_ds.products"

def remove_basket(product):
    r = requests.get("https://us-central1-cmpe48a-project.cloudfunctions.net/removing_from_basket",
                     headers={"key": "efebugra","user_name": "Bugra", "product_id": product})
    print(r)



