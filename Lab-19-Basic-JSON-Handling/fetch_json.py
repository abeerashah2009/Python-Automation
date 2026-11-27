import json
import requests

api_url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(api_url, timeout=10)
response.raise_for_status()

data = response.json()

# Extract specific information
post_info = {
    "title": data["title"],
    "body": data["body"]
}

# Save data into a JSON file
with open("post_info.json", "w") as json_file:
    json.dump(post_info, json_file, indent=4)

print("Data saved to post_info.json")
