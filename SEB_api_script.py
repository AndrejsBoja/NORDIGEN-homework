import requests, json

accounts = "https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts"
transactions = "https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/6e367bd7-581a-48da-af3b-3406d4c9247b/transactions?bookingStatus=booked"

headers = {
  'Accept': 'application/json',
  'X-Request-ID': '35fb5b7a-a183-454f-9cc5-f6bdb7d68e78',
  'PSU-IP-Address': '130.55.114.104',
  'Authorization': 'Bearer REPLACE_TOKEN',
  'Cookie': 'C0WNET=17c40a6c-60de-444a-a478-196e74575c08'
}

response = requests.request("GET", transactions, headers=headers)

parsed = json.loads(response.text)

print(json.dumps(parsed, indent=4, sort_keys=True))