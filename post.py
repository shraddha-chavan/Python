import requests
url="https://jsonplaceholder.typicode.com/users"
data={
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response= requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response Data:")
print(response.json())