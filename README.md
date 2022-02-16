# Australian Open Banking Data Database
<img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/Uskompuf/Australian-Open-Banking-Data-Database.svg?sanitize=true"/><img alt="GitHub Time Since Last Commit" src="https://img.shields.io/github/last-commit/Uskompuf/Australian-Open-Banking-Data-Database.svg?sanitize=true"/>

On 26 November 2017, the Australian Government announced the introduction of a consumer data right (CDR) in Australia. The CDR will first apply to the banking sector with a [phased introduction](#phasing-table), currently the only publically available data is product reference data which includes credit and debit cards, deposit accounts, transaction accounts, mortgages, and personal loans. Consumer data is only available to [acreddited institutions](https://www.cdr.gov.au/find-a-provider?providerType=Data%2520Recipient). Personal access to consumer data is set to be implemented by major and non-major ADIs post 1 November 2021

This repositry is an ongoing collection of Open Banking Data API endpoint URLs for Australian deposit taking institutions. The API specifications for these endpoints can be found [here](https://consumerdatastandardsaustralia.github.io/standards/#future-dated-obligations).

## Getting Started ##

To access any product reference data you need to send a HTTP request with the required parameters to the appropraite banking API URL. The two available Banking APIs are [Get Products](https://consumerdatastandardsaustralia.github.io/standards/#get-products) and [Get Product Detail](https://consumerdatastandardsaustralia.github.io/standards/#get-product-detail).

The easiest way to get started is the Swagger UI [page](https://generator.swagger.io/?url=https://raw.githubusercontent.com/LukePrior/Australian-Open-Banking-Data-Database/main/examples/CDS-Products.yaml) which has all the endpoints imported and the required fields documented.

**Get Products**

This API returns a list of products currently offered by the financial institution to the market.

`https://data.holder.com.au/cds-au/v1/banking/products`

You can run the following example from CMD.

`curl -X GET https://api.anz/cds-au/v1/banking/products -H "x-v: 3"`

**Get Product Detail**

This API returns detailed information on a single product offered by the financial institutions.

`https://data.holder.com.au/cds-au/v1/banking/products/{productId}`

You can run the following example from CMD.

`curl -X GET https://api.anz/cds-au/v1/banking/products/5eb62ffc-51f0-6ac0-2abf-d81b260ee260 -H "x-v: 3"`

## Examples

- You can use the [Swagger UI](https://generator.swagger.io/?url=https://raw.githubusercontent.com/LukePrior/Australian-Open-Banking-Data-Database/main/examples/CDS-Products.yaml) to easily test the APIs for any bank.
- Examples for the Get Products and Get Product Detail APIs can be found [here](EXAMPLES.md). The examples are available in PHP, JavaScript, Python, C#, and Curl.
- A jupyter notebook is available to download [here](examples/Australian_Open_Banking_Data.ipynb) or you can run the examples online with [Google Colab](https://colab.research.google.com/drive/1P_Tlww5VWMXJx7qhmISrhaqgxbF-yZRs#offline=true&sandboxMode=true).

## List of Current Providers - 113

This is the current list of Australian deposit taking institutions and their respective CDS API endpoints. The insitutions have been classified into unique categories, the complete unsorted list of API endpoints can be found [here](raw/complete.txt).


**Big Four Banks**
```
Australia and New Zealand Banking Group (ANZ): https://api.anz/cds-au/v1
Commonwealth Bank of Australia (CBA): https://api.commbank.com.au/public/cds-au/v1
National Australia Bank (NAB): https://openbank.api.nab.com.au/cds-au/v1
Westpac Banking Corporation (Westpac): https://digital-api.westpac.com.au/cds-au/v1
```

**Regional Banks**
```
Bank of Queensland (BOQ): https://secure.api.boq.com.au/cds-au/v1
Macquarie Bank: https://api.macquariebank.io/cds-au/v1
Bendigo Bank: https://api.cdr.bendigobank.com.au/cds-au/v1
Adelaide Bank: https://api.cdr.adelaidebank.com.au/cds-au/v1
AMP: https://api.cdr-api.amp.com.au/cds-au/v1
Suncorp: https://id-ob.suncorpbank.com.au/cds-au/v1
ING Bank: https://apic.ing.com.au/cds-au/v1
HSBC Bank: https://openbanking.hsbc.com.au/cds-au/v1 
```

**Small Banks**
```
AWA Alliance Bank: https://api.cdr.awaalliancebank.com.au/cds-au/v1
Arab Bank Australia: https://openbanking-api.arabbank.com.au/public/cds-au/v1
Australian Mutual Bank: https://internetbanking.australianmutual.bank/openbanking/cds-au/v1
Australian Unity Bank: https://open-banking.australianunity.com.au/cds-au/v1
Auswide Bank: https://api.auswidebank.com.au/OpenBanking/cds-au/v1
BDCU Alliance Bank: https://api.cdr.bdcualliancebank.com.au/cds-au/v1
Bank Australia: https://cds.api.bankaust.com.au/cds-au/v1
Bank of China Australia: https://obdevp.bank-of-china.net.au/cds-au/v1
Bank of Melbourne: https://digital-api.bankofmelbourne.com.au/cds-au/v1
Bank of Sydney: https://openbank.api.banksyd.com.au/cds-au/v1
Bank of us: https://api.bankofus.com.au/OpenBanking/cds-au/v1
BankSA: https://digital-api.banksa.com.au/cds-au/v1
Bankwest: https://open-api.bankwest.com.au/bwpublic/cds-au/v1
Beyond Bank Australia: https://public.cdr.api.beyondbank.com.au/cds-au/v1
BOQ Specialist: https://secure.api.boqspecialist.com.au/cds-au/v1
Cairns Bank: https://ibanking.cairnsbank.com.au/openbanking-penny/cds-au/v1
Circle Alliance Bank: https://api.cdr.circle.com.au/cds-au/v1
Citibank: https://aspac.api.citi.com/gcb/cds-au/v1
First Option Bank: https://internetbanking.firstoption.com.au/OpenBanking/cds-au/v1
G&C Mutual Bank: https://ibank.gcmutualbank.com.au/openbanking/cds-au/v1
Gateway Bank: https://public.cdr-api.gatewaybank.com.au/cds-au/v1
Geelong Bank: https://online.geelongbank.com.au/OpenBanking/cds-au/v1
Goldfields Money: https://prd.bnk.com.au/cds-au/v1
Greater Bank: https://public.cdr-api.greater.com.au/cds-au/v1
Heritage Bank: https://product.api.heritage.com.au/cds-au/v1
Horizon Bank: https://onlinebanking.horizonbank.com.au/openbanking/cds-au/v1
Hume Bank: https://ibank.humebank.com.au/openbanking/cds-au/v1
IMB Bank: https://openbank.openbanking.imb.com.au/cds-au/v1
Judo Bank: https://public.open.judo.bank/cds-au/v1
ME Bank: https://api.mebank.com.au/cds-au/v1
MOVE Bank: https://api.movebank.com.au/OpenBanking/cds-au/v1
MyLife MyFinance: https://openbanking-api.mylifemyfinance.com.au/cds-au/v1
MyState Bank: https://openbank.api.mystate.com.au/cds-au/v1
Nova Alliance Bank: https://api.cdr.novaalliancebank.com.au/cds-au/v1
Qudos Bank: https://public.cdr-api.qudosbank.com.au/cds-au/v1
Queensland Country Bank: https://public.cdr-api.queenslandcountry.bank/cds-au/v1
RACQ Bank: https://cdrbank.racq.com.au/cds-au/v1
Rabobank: https://openbanking.api.rabobank.com.au/cds-au/v1
RAMS Financial Group: https://digital-api.westpac.com.au/rams/cds-au/v1
Regional Australia Bank: https://public-data.cdr.regaustbank.io/cds-au/v1
Rural Bank: https://api.cdr.ruralbank.com.au/cds-au/v1
Service One Alliance Bank: https://api.cdr.serviceone.com.au/cds-au/v1
St.George Bank: https://digital-api.stgeorge.com.au/cds-au/v1
UBank: https://openbank.api.ubank.com.au/cds-au/v1
Unity Bank: https://ibanking.unitybank.com.au/OpenBanking/cds-au/v1
Virgin Money Australia: https://secure.api.virginmoney.com.au/cds-au/v1
```

**Credit Unions**
```
Bank First: https://public.cdr.bankfirst.com.au/cds-au/v1
Broken Hill Community Credit Union: https://public.cdr-api.bhccu.com.au/cds-au/v1
Central Murray Credit Union: https://secure.cmcu.com.au/openbanking/cds-au/v1
Central West Credit Union: https://ib.cwcu.com.au/openbanking/cds-au/v1
Coastline Credit Union: https://public.cdr-api.coastline.com.au/cds-au/v1
Community First Credit Union: https://netbank.communityfirst.com.au/cf-openbanking/cds-au/v1
Credit Union SA: https://openbanking.api.creditunionsa.com.au/cds-au/v1
Dnister Ukrainian Credit Co-operative: https://public.cdr-api.dnister.com.au/cds-au/v1
Easy Street Financial Services: https://ebranch.easystreet.com.au/es-openbanking/cds-au/v1
Family First Credit Union: https://online.familyfirst.com.au/OpenBanking/cds-au/v1
First Choice Credit Union: https://public.cdr-api.firstchoicecu.com.au/cds-au/v1
Goulburn Murray Credit Union: https://gmcu.cds.cuscal.com.au/cds-au/v1
Great Southern Bank: https://api.open-banking.greatsouthernbank.com.au/cds-au/v1
Illawarra Credit Union: https://onlineteller.cu.com.au/OpenBanking/cds-au/v1
Laboratories Credit Union: https://internetbanking.lcu.com.au/openbanking/cds-au/v1
Macquarie Credit Union: https://banking.macquariecu.com.au/OpenBanking/cds-au/v1
The Mutual Bank: https://openbanking.themutual.com.au/OpenBanking/cds-au/v1
Newcastle Permanent Building Society: https://api.newcastlepermanent.com.au/cds-au/v1
Northern Inland Credit Union: https://api.cds.nicu.com.au/cds-au/v1
Orange Credit Union: https://online.orangecu.com.au/openbanking/cds-au/v1
People's Choice Credit Union: https://ob-public.peopleschoice.com.au/public/cds-au/v1
Pulse Credit Union: https://public.cdr-api.pulsecredit.com.au/cds-au/v1
South West Credit Union: https://internetbanking.swcredit.com.au/OpenBanking/cds-au/v1
South West Slopes Credit Union: https://online.swscu.com.au/OpenBanking/cds-au/v1
Southern Cross Credit Union: https://mvp1.sccu.com.au/OpenBanking/cds-au/v1
Summerland Credit Union: https://public.cdr-api.summerland.com.au/cds-au/v1
The Capricornian: https://onlinebanking.capricornian.com.au/OpenBanking/cds-au/v1
The Mac Credit Union: https://onlinebanking.themaccu.com.au/OpenBanking/cds-au/v1
Transport Mutual Credit Union: https://banking.transportmutual.com.au/OpenBanking/cds-au/v1
WAW Credit Union: https://onlinebanking.wawcu.com.au/OpenBanking/cds-au/v1
Warwick Credit Union: https://ibanking.wcu.com.au/openbanking-warwick/cds-au/v1
bcu: https://ob-api.bcu.com.au/cds-au/v1
```

**Neobanks / Other**
```
86 400: https://public.cdr-api.86400.com.au/cds-au/v1
Leveraged: https://api.cdr.leveraged.com.au/cds-au/v1
Money by Afterpay: https://api.cds.afterpay.com.au/cds-au/v1
PayPal: https://api.paypal.com/v1/identity/cds-au/v1
Tyro: https://public.cdr.tyro.com/cds-au/v1
Up: https://api.up.com.au/cds-au/v1
Volt Bank: https://api.voltbank.com.au/cds-au/v1
```

**Selective Banks / Credit Unions**
```
Australian Military Bank: https://public.open.australianmilitarybank.com.au/cds-au/v1
BankVic: https://ib.bankvic.com.au/openbanking/cds-au/v1
Defence Bank: https://product.defencebank.com.au/cds-au/v1
Firefighters Mutual Bank: https://ob.tmbl.com.au/fmbank/cds-au/v1
Fire Service Credit Union: https://public.cdr-api.fscu.com.au/cds-au/v1
Health Professionals Bank: https://ob.tmbl.com.au/hpbank/cds-au/v1
Hiver Bank: https://ob.tmbl.com.au/hiver/cds-au/v1
P&N Bank: https://ob-api.pnbank.com.au/cds-au/v1
Police Bank: https://product.api.policebank.com.au/cds-au/v1
Police Credit Union: https://api.policecu.com.au/openbanking/cds-au/v1
QBANK: https://banking.qbank.com.au/openbanking/cds-au/v1
RSL Money: https://public.open.rslmoney.com.au/cds-au/v1
Teachers Mutual Bank: https://ob.tmbl.com.au/tmbank/cds-au/v1
Traditional Credit Union: https://prd.tcu.com.au/cds-au/v1
Unibank: https://ob.tmbl.com.au/unibank/cds-au/v1
Woolworths Team Bank: https://online.woolworthsteambank.com.au/OpenBanking/cds-au/v1
```

*NOTE: CitiBank also requires the `Accept: application/json` header to be sent*

## Consumer Data Right Register

This API returns all active Consumer Data Right Holders and Recipients.

https://api.cdr.gov.au/cdr-register/v1/banking/register

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
