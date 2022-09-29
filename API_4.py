#4.

import requests
import json

url = "https://reqres.in/api/users/"

payload = json.dumps({
  "name": "Pepe"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response)
