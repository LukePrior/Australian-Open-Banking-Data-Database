import requests
import re

brands = {}

r = requests.get(
    'https://api.cdr.gov.au/cdr-register/v1/banking/data-holders/brands/summary', 
    headers={
        "x-v":"1",
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
    }
)

available_brands = r.json()
sorted_brands = sorted(available_brands['data'], key=lambda item: item['brandName'])

f = open("raw/complete.txt", "w", encoding="utf8", errors='ignore')
for brand in sorted_brands:
    f.write(f"{brand['brandName']}: {brand['publicBaseUri']}/cds-au/v1\n")
f.close()

f = open("README.md", "r", encoding="utf8", errors='ignore')
readme = f.read()
f.close()

readme = re.sub(r"<!-- BRANDS -->.*<!-- /BRANDS -->", "<!-- BRANDS -->\n```\n" + "\n".join([f"{brand['brandName']}: {brand['publicBaseUri']}/cds-au/v1" for brand in sorted_brands]) + "\n```\n<!-- /BRANDS -->", readme, flags=re.DOTALL)
readme = re.sub(r"<!-- COUNT -->.*<!-- /COUNT -->", f"<!-- COUNT -->{len(sorted_brands)}<!-- /COUNT -->", readme, flags=re.DOTALL)

f = open("README.md", "w")
f.write(readme)
f.close()