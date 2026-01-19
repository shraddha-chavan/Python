import requests
url="https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print("Status Code:", response.status_code)
print("Response Data:")
print(response.json())  
users=response.json()
for user in users:
    print("Name:", user['name'])
    print("Email:", user['email'])
    print("City:", user['address']['city'])
    print("Phone:", user['phone'])
    print("address:",user['address'].get("city"))#alternative way to access city

    print("---------------------------")