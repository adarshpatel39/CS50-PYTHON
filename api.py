import json
import requests
import sys

if len(sys.argv)!=2 :
  sys.exit()

response=requests.get("https://open.spotify.com/user/31csclxx3vkvaqzwhon2rdsrwkh4" + sys.argv[1])

print(json.dumps(response.json(),indent=2))
print(response.json())
# o=response.json()
# for result in o["results"] :
#   print(result["trackName"])