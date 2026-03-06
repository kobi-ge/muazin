import requests
import json


def post_to_kibana(index_name):
    kibana_url = "http://localhost:5601/api/data_views/data_view"
    payload = {
        "data_view": {
            "title": index_name, 
            "name": "My Data View" 
            }
        }
    headers = {
        "Content-Type": "application/json",
        "kbn-xsrf": "true"
        }
    response = requests.post(kibana_url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        print("Data View created successfully!")
        return response.json()
    else:
        print(f"Failed to create Data View. Status code: {response.status_code}")
        print(response.text)