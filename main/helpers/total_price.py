import ast
import json
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/efesabanoglu/Downloads/cmpe48a-project-ecce664060c5.json'
from google.cloud import bigquery
import requests

SOURCE_TABLE = "cmpe48a-project.product_ds.products"

def get_total_price():
    r = requests.get("https://us-central1-cmpe48a-project.cloudfunctions.net/get_total_price",
                     headers={"key": "efebugra", "user_name": "Bugra"})
    content = json.loads(r.content.decode("UTF-8"))
    return content