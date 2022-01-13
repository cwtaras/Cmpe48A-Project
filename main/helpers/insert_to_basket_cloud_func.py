import ast
import json
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/bugra/Downloads/cmpe48a-project-434fa4ee5f87.json'
from google.cloud import bigquery
import requests

SOURCE_TABLE = "cmpe48a-project.product_ds.products"

def add_basket(product):
    r = requests.get("https://us-central1-cmpe48a-project.cloudfunctions.net/adding_product_to_basket",
                     headers={"key": "efebugra","user_name" : "Bugra", "product_name": product})
    print(r)



