import re
import requests
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["x-v"] = "2"

f = open("complete.txt", "r")
for x in f:
  urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', x)
  url = urls[0] + "/banking/products"

  try:
      resp = requests.get(url, headers=headers, verify=True)
      time = resp.elapsed.total_seconds()
      if resp.status_code == 200:
          print(str(urls[0]) + " | " + str(time) + "s")
  except Exception as e:
      print("ERROR: " + str(e))





