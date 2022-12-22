import requests
# import json

response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
response.raise_for_status()

data = response.json()

# print(json.dumps(data, indent=2))

question_data = data["results"]
