import requests

response = requests.post(
    "http://localhost:5000/receive_model",
    json={"model_name": "bert-base-uncased"}
)
print(response.json())