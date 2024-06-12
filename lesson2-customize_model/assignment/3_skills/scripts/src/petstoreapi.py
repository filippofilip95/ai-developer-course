import requests

url = "https://petstore.swagger.io/v2/store/order"
headers = {
    "Content-Type": "application/json"
}
order_payload = {
    "id": 0,
    "petId": 0,
    "quantity": 1,
    "shipDate": "2023-01-01T00:00:00Z",
    "status": "placed",
    "complete": False
}

response = requests.post(url, headers=headers, json=order_payload)

print(response.status_code)
print(response.json())