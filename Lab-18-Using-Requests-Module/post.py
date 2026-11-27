import sys
import requests

URL = sys.argv[1] if len(sys.argv) > 1 else "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(URL, timeout=10)
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
    sys.exit(1)

if response.status_code == 200:
    print("Request was successful!")
else:
    print(f"Request failed with status code: {response.status_code}")
    sys.exit(1)

data = response.json()

print(f"Title: {data['title']}")
print(f"Body: {data['body']}")
