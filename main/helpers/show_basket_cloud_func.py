import ast
import json
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='C:/Users/bugra/Downloads/cmpe48a-project-434fa4ee5f87.json'
from google.cloud import bigquery
import requests

SOURCE_TABLE = "cmpe48a-project.product_ds.products"

def show_basket():
    r = requests.get("https://us-central1-cmpe48a-project.cloudfunctions.net/show_basket",
                     headers={"key": "efebugra","user_name": "Bugra"})
    content = json.loads(r.content.decode("UTF-8"))
    return content



