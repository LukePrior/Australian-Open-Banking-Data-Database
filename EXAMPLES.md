# Open Banking Data API Examples

Here are some fully working code examples to utilise the Get Products and Get product Detail API's.

## Get Products

This API returns a list of products currently offered by the financial institution to the market.

`https://data.holder.com.au/cds-au/v1/banking/products`

**PHP**

```
<?php

$url = "https://api.anz/cds-au/v1/banking/products";

$curl = curl_init($url);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$headers = array(
   "x-v: 2",
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

**Python**

**C#**

**Curl**

## Get Product Detail

This API returns detailed information on a single product offered by the financial institutions.

`https://data.holder.com.au/cds-au/v1/banking/products/{productId}`
