import requests
# import json

response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")

data = response.json()

# print(json.dumps(data, indent=2))

question_data = data["results"]
