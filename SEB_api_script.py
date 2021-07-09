import requests, json

accounts = "https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts"
transactions = "https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/6e367bd7-581a-48da-af3b-3406d4c9247b/transactions?bookingStatus=booked"

headers = {
  'Accept': 'application/json',
  'X-Request-ID': '9c61f71e-eb40-4f0a-aeba-a71c7e6a6bba',
  'PSU-IP-Address': '14.212.5.47',
  'Authorization': 'Bearer zhj25iD1rASdXzvvNadY',
  'Cookie': 'C0WNET=17c40a6c-60de-444a-a478-196e74575c08; AMWEBJCT!%2Fmga!JSESSIONID=0000QXS2kmsndv8nRqf-cT8HsGi:938ed943-3c20-4801-ace0-52dd1dd31f86; PD-SESSION-ID=1_4_1_74dAcAo1Ei7BEeg9Nm+V5sAwRGsCjeiFjclFCf1Uu7rSpUPp; PGNET=77ab66f5-60e8-49c3-a15f-4ad27ccf2204; TS01136fc4=0107224bedcd55b1550d27fb97ae585dc525bb2d9e2b8621abd96bcccf6812f5668a3588076cc3154c81feb2399d6efc241b9017bc; TS018787d1=0107224bed09a67cc3d374acabcad9aec8d2d28ac43728a2e55aad0ce8d060a23b94ce46b28145b0e89a820f7a2e0a5124e9f1997a'
}

response = requests.request("GET", transactions, headers=headers)

parsed = json.loads(response.text)

print(json.dumps(parsed, indent=4, sort_keys=True))