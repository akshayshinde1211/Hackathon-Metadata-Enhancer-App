import requests
import json

url = "http://127.0.0.1:8000/api/generate"

files = {
    'schema_file': ('schema.json', open('test_data/schema.json', 'rb'), 'application/json'),
    'sample_data_file': ('data.csv', open('test_data/data.csv', 'rb'), 'text/csv')
}

try:
    response = requests.post(url, files=files)
    if response.status_code == 200:
        print("SUCCESS: API returned 200")
        print("Response:", json.dumps(response.json(), indent=2))
    else:
        print(f"FAILURE: API returned {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"ERROR: {e}")
