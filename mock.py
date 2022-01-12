from main.helpers.get_products_cloud_func import get_products
import requests
import json

if __name__ == "__main__":
    r = requests.get("https://us-central1-cmpe48a-project.cloudfunctions.net/get_total_price",
                     headers={"key": "efebugra", "user_name": "Bugra"})
    content = json.loads(r.content.decode("UTF-8"))
    print(type(content))