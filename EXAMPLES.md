# Open Banking Data API Examples

Here are some fully working code examples to utilise the Get Products and Get product Detail API's.

## Get Products

This API returns a list of products currently offered by the financial institution to the market.

`https://data.holder.com.au/cds-au/v1/banking/products`

**PHP**

```PHP
<?php

$url = "https://api.anz/cds-au/v1/banking/products";

$curl = curl_init($url);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$headers = array(
   "x-v: 3",
);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
//for debug only!
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

$resp = curl_exec($curl);
curl_close($curl);
var_dump($resp);

?>
```

**JavaScript**

```JavaScript
const proxyurl = "https://cors-anywhere.herokuapp.com/";

var url = "https://api.anz/cds-au/v1/banking/products";

var xhr = new XMLHttpRequest();
xhr.open("GET", proxyurl + url);

xhr.setRequestHeader("x-v", "3");

xhr.onreadystatechange = function () {
   if (xhr.readyState === 4) {
      console.log(xhr.status);
      console.log(xhr.responseText);
   }};

xhr.send();
```

**Python**

```Python
import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.anz/cds-au/v1/banking/products"

headers = CaseInsensitiveDict()
headers["x-v"] = "3"

resp = requests.get(url, headers=headers)

print(resp.content)
```

**C#**

```C#
var url = "https://api.anz/cds-au/v1/banking/products";

var httpRequest = (HttpWebRequest)WebRequest.Create(url);

httpRequest.Headers["x-v"] = "3";

var httpResponse = (HttpWebResponse)httpRequest.GetResponse();
using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
{
   var result = streamReader.ReadToEnd();
   Console.WriteLine(result);
}
```

**Curl**

```
#!/bin/bash

curl -X GET https://api.anz/cds-au/v1/banking/products -H "x-v: 3" 
```

## Get Product Detail

This API returns detailed information on a single product offered by the financial institutions.

`https://data.holder.com.au/cds-au/v1/banking/products/{productId}`

**PHP**

```PHP
<?php

$url = "https://api.anz/cds-au/v1/banking/products/5eb62ffc-51f0-6ac0-2abf-d81b260ee260";

$curl = curl_init($url);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$headers = array(
   "x-v: 3",
);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
//for debug only!
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

$resp = curl_exec($curl);
curl_close($curl);
var_dump($resp);

?>
```

**JavaScript**

```JavaScript
const proxyurl = "https://cors-anywhere.herokuapp.com/";

var url = "https://api.anz/cds-au/v1/banking/products/5eb62ffc-51f0-6ac0-2abf-d81b260ee260";

var xhr = new XMLHttpRequest();
xhr.open("GET", proxyurl + url);

xhr.setRequestHeader("x-v", "3");

xhr.onreadystatechange = function () {
   if (xhr.readyState === 4) {
      console.log(xhr.status);
      console.log(xhr.responseText);
   }};

xhr.send();
```

**Python**

```Python
import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.anz/cds-au/v1/banking/products/5eb62ffc-51f0-6ac0-2abf-d81b260ee260"

headers = CaseInsensitiveDict()
headers["x-v"] = "3"

resp = requests.get(url, headers=headers)

print(resp.content)
```

**C#**

```C#
var url = "https://api.anz/cds-au/v1/banking/products/5eb62ffc-51f0-6ac0-2abf-d81b260ee260";

var httpRequest = (HttpWebRequest)WebRequest.Create(url);

httpRequest.Headers["x-v"] = "3";

var httpResponse = (HttpWebResponse)httpRequest.GetResponse();
using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
{
   var result = streamReader.ReadToEnd();
   Console.WriteLine(result);
}
```

**Curl**

```
#!/bin/bash

curl -X GET https://api.anz/cds-au/v1/banking/products/5eb62ffc-51f0-6ac0-2abf-d81b260ee260 -H "x-v: 3" 
```
