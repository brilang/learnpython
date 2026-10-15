import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Define the API endpoint URL
url = 'https://randomuser.me/api/'
params = {
    "results": 10,
    "seed": os.getenv('SEED')
}
# Send the GET request
res = requests.get(url, params=params)

# Check if the request was successful (HTTP Status Code 200)
if res.status_code == 200:
    # Convert JSON response into a Python dictionary
    data = res.json()
    print("Success!")
else:
    print(f"Failed with status code: {res.status_code}")

if(data):
    # print(json.dumps(data['results'], indent=2))
    print(json.dumps(data['results'][2], indent=4, ensure_ascii=False))