import requests
import json

getAccounts = "https://sandbox.handelsbanken.com/openbanking/psd2/v2/accounts"
getTransactions = "https://sandbox.handelsbanken.com/openbanking/psd2/v2/accounts/ae5883c0-6cf3-11e9-9c41-e957ce7d7d69/transactions"

headers = {
    'Authorization': 'Bearer REPLACE_TOKEN',
    'PSU-IP-Address': '192.102.28.2',
    'TPP-Request-ID': 'c8271b81-4229-5a1f-bf9c-758f11c1f5b1',
    'TPP-Transaction-ID': '6b24ce42-237f-4303-a917-cf778e5013d6',
    'X-IBM-Client-Id': '62dec6b3-1814-4ca2-864a-c33b91ef6007',
    'Accept': 'application/json'
}

response = requests.request("GET", getAccounts, headers=headers)

parsed = json.loads(response.text)

print(json.dumps(parsed, indent=4, sort_keys=True))