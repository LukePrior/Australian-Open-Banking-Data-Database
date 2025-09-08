# Australian Open Banking Data Database
<img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/Uskompuf/Australian-Open-Banking-Data-Database.svg?sanitize=true"/><img alt="GitHub Time Since Last Commit" src="https://img.shields.io/github/last-commit/Uskompuf/Australian-Open-Banking-Data-Database.svg?sanitize=true"/>

On 26 November 2017, the Australian Government announced the introduction of a consumer data right (CDR) in Australia. The CDR has been fully rolled out in the banking sector with energy and telco sectors set to be included in the coming years. Consumer data is only available to [acreddited institutions](https://www.cdr.gov.au/find-a-provider?providerType=Data%2520Recipient).

This repositry is an ongoing collection of Open Banking Data API endpoint URLs for Australian deposit taking institutions. This list used to be manually generated but has since switched to using the Data Holder Brands Summary [API](https://www.cdr.gov.au/for-providers/how-find-data-holders-product-data-request-service) The API specifications for these endpoints can be found [here](https://consumerdatastandardsaustralia.github.io/standards/#future-dated-obligations).

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

## List of Current Providers - <!-- COUNT -->120<!-- /COUNT -->

This is the current list of Australian deposit taking institutions and their respective CDS API endpoints. The complete unsorted list of API endpoints can be found [here](raw/complete.txt).

<!-- BRANDS -->
```
AMP - My AMP: https://api.cdr-api.amp.com.au/cds-au/v1
AMP Bank GO: https://pub.cdr-sme.amp.com.au/api/cds-au/v1
ANZ: https://api.anz/cds-au/v1
ANZ Plus: https://cdr.apix.anz/cds-au/v1
Adelaide Bank: https://api.cdr.adelaidebank.com.au/cds-au/v1
Alex.Bank: https://public.cdr.alex.com.au/cds-au/v1
Arab Bank Australia Limited: https://public.cdr.arabbank.com.au/cds-au/v1
Aussie Home Loans: https://aussie.openportal.com.au/cds-au/v1
Australian Military Bank: https://public.open.australianmilitarybank.com.au/cds-au/v1
Australian Mutual Bank LTD: https://internetbanking.australianmutual.bank/openbanking/cds-au/v1
Australian Unity Bank: https://open-banking.australianunity.com.au/cds-au/v1
Auswide Bank Ltd: https://api.auswidebank.com.au/openbanking/cds-au/v1
BCU Bank: https://public.cdr-api.bcu.com.au/cds-au/v1
BNK Bank (Goldfields Money/BCHL): https://public.cdr.bnk.com.au/cds-au/v1
BOQ Specialist: https://api.cds.boqspecialist.com.au/cds-au/v1
Bank Australia: https://public.cdr.bankaust.com.au/cds-au/v1
Bank First: https://public.cdr.bankfirst.com.au/cds-au/v1
Bank of China: https://api-gateway.bankofchina.com.au/cds-au/v1
Bank of Melbourne: https://digital-api.bankofmelbourne.com.au/cds-au/v1
Bank of Queensland Limited: https://api.cds.boq.com.au/cds-au/v1
Bank of Sydney: https://openbank.api.banksyd.com.au/cds-au/v1
Bank of us: https://api.bankofus.com.au/OpenBanking/cds-au/v1
BankSA: https://digital-api.banksa.com.au/cds-au/v1
BankVic: https://ib.bankvic.com.au/openbanking/cds-au/v1
Bankwest: https://open-api.bankwest.com.au/bwpublic/cds-au/v1
Bendigo Bank: https://api.cdr.bendigobank.com.au/cds-au/v1
Beyond Bank Australia: https://public.cdr.api.beyondbank.com.au/cds-au/v1
Border Bank: https://public.cdr.prd.borderbank.com.au/cds-au/v1
Broken Hill Bank: https://public.cdr-api.bhccu.com.au/cds-au/v1
CBA - CommBiz: https://cdr.commbiz.api.commbank.com.au/cbzpublic/cds-au/v1
Cairns bank: https://openbanking.cairnsbank.com.au/OpenBanking/cds-au/v1
Card Services: https://api.openbanking.cardservicesdirect.com.au/cds-au/v1
Central Murray Bank: https://secure.cmcu.com.au/openbanking/cds-au/v1
Central West CUL: https://ib.cwcu.com.au/openbanking/cds-au/v1
Citi: https://openbanking.api.citi.com.au/cds-au/v1
Coastline Bank: https://public.cdr-api.coastline.com.au/cds-au/v1
Coles Credit Cards: https://api.openbanking.secure.coles.com.au/cds-au/v1
CommBank: https://api.commbank.com.au/public/cds-au/v1
CommFCU: https://netbank.communityfirst.com.au/cf-OpenBanking/cds-au/v1
Credit Union SA: https://openbanking.api.creditunionsa.com.au/cds-au/v1
DDH Graham: https://api.cds.ddhgraham.com.au/cds-au/v1
Darling Downs Bank: https://openbanking.wcu.com.au/OpenBanking/cds-au/v1
Defence Bank: https://product.defencebank.com.au/cds-au/v1
Dnister: https://public.cdr-api.dnister.com.au/cds-au/v1
Easy Street: https://ebranch.easystreet.com.au/es-OpenBanking/cds-au/v1
Family First: https://public.cdr.familyfirst.com.au/cds-au/v1
Fire Service Credit Union: https://public.cdr-api.fscu.com.au/cds-au/v1
Firefighters Mutual Bank: https://ob.tmbl.com.au/fmbank/cds-au/v1
First Option Bank: https://internetbanking.firstoption.com.au/OpenBanking/cds-au/v1
G&C Mutual Bank: https://ibank.gcmutualbank.com.au/OpenBanking/cds-au/v1
Gateway Bank: https://public.cdr-api.gatewaybank.com.au/cds-au/v1
Geelong Bank: https://online.geelongbank.com.au/OpenBanking/cds-au/v1
Great Southern Bank: https://api.open-banking.greatsouthernbank.com.au/cds-au/v1
Great Southern Bank Business+: https://od1.open-banking.business.greatsouthernbank.com.au/api/cds-au/v1
Greater Bank Limited: https://public.cdr.greater.com.au/cds-au/v1
HSBC: https://public.ob.hsbc.com.au/cds-au/v1
HSBC Bank Australia Limited – Wholesale Banking: https://public.ob.business.hsbc.com.au/cds-au/v1
Health Professionals Bank: https://ob.tmbl.com.au/hpbank/cds-au/v1
Heartland: https://api.cdr.heartlandbank.com.au/cds-au/v1
Heritage Bank. Please do not use, please use People’s Choice.: https://product.api.heritage.com.au/cds-au/v1
Horizon Bank: https://onlinebanking.horizonbank.com.au/openbanking/cds-au/v1
Hume Bank: https://ibankob.humebank.com.au/OpenBanking/cds-au/v1
IMB Bank: https://openbank.openbanking.imb.com.au/cds-au/v1
ING BANK (Australia) Ltd: https://id.ob.ing.com.au/cds-au/v1
Illawarra Credit Union Limited: https://onlineteller.cu.com.au/OpenBanking/cds-au/v1
Judo Bank: https://public.open.judo.bank/cds-au/v1
Kogan Money Credit Cards: https://api.openbanking.cards.koganmoney.com.au/cds-au/v1
Laboratories Credit Union: https://internetbanking.lcu.com.au/OpenBanking/cds-au/v1
Liberty Financial: https://services.liberty.com.au/api/data-holder-public/cds-au/v1
ME Bank: https://public.openbank.mebank.com.au/cds-au/v1
ME Bank - ME Go: https://api.cds.mebank.com.au/cds-au/v1
MOVE Bank: https://openbanking.movebank.com.au/OpenBanking/cds-au/v1
Macquarie Bank Limited: https://api.macquariebank.io/cds-au/v1
Maitland Mutual Limited: https://openbanking.themutual.com.au/OpenBanking/cds-au/v1
MyState Bank: https://public.cdr.mystate.com.au/cds-au/v1
NATIONAL AUSTRALIA BANK: https://openbank.api.nab.com.au/cds-au/v1
Newcastle Permanent Building Society: https://openbank.newcastlepermanent.com.au/cds-au/v1
Northern Inland Credit Union Limited: https://secure.nicu.com.au/OpenBanking/cds-au/v1
ORANGE CREDIT UNION LTD: https://online.orangecu.com.au/openbanking/cds-au/v1
P&N Bank: https://public.cdr-api.pnbank.com.au/cds-au/v1
PayPal Australia: https://api.paypal.com/v1/identity/cds-au/v1
People's Choice: https://ob-public.peopleschoice.com.au/cds-au/v1
Police Bank: https://public.cdr.prd.policebank.com.au/cds-au/v1
Police Credit Union Ltd: https://api.policecu.com.au/OpenBanking/cds-au/v1
QBANK: https://banking.qbank.com.au/openbanking/cds-au/v1
Qantas Money Credit Cards: https://api.openbanking.qantasmoney.com/cds-au/v1
Qudos Bank: https://public.cdr.qudosbank.com.au/cds-au/v1
Queensland Country Bank: https://public.cdr-api.queenslandcountry.bank/cds-au/v1
RACQ Bank: https://cdrbank.racq.com.au/cds-au/v1
RAMS Financial Group Pty Ltd: https://digital-api.westpac.com.au/rams/cds-au/v1
RSL Money: https://public.open.rslmoney.com.au/cds-au/v1
Rabobank: https://openbanking.api.rabobank.com.au/public/cds-au/v1
Regional Australia Bank: https://public-data.cdr.regaustbank.io/cds-au/v1
Reliance Bank: https://ibanking.reliancebank.com.au/rel-openbanking/cds-au/v1
SWSbank: https://online.swsbank.com.au/openbanking/cds-au/v1
Solo by MYOB: https://od1.open-banking.myob.greatsouthernbank.com.au/api/cds-au/v1
Southern Cross Credit Union: https://cdr.sccu.com.au/openbanking/cds-au/v1
St.George Bank: https://digital-api.stgeorge.com.au/cds-au/v1
Summerland Bank: https://public.cdr-api.summerland.com.au/cds-au/v1
Suncorp Bank: https://id-ob.suncorpbank.com.au/cds-au/v1
TMCU: https://banking.transportmutual.com.au/OpenBanking/cds-au/v1
Teachers Mutual Bank: https://ob.tmbl.com.au/tmbank/cds-au/v1
The Capricornian: https://public.cdr.onlinebanking.capricornian.com.au/cds-au/v1
The Mac: https://onlinebanking.themaccu.com.au/OpenBanking/cds-au/v1
Thriday: https://public.cdr.thriday.com.au/cds-au/v1
Traditional Credit Union: https://prd.tcu.com.au/cds-au/v1
Tyro Banking: https://od1.cdr.banking.tyro.com/api/cds-au/v1
Tyro Payments: https://public.cdr.tyro.com/cds-au/v1
UBank: https://public.cdr-api.86400.com.au/cds-au/v1
UniBank: https://ob.tmbl.com.au/unibank/cds-au/v1
Unity Bank: https://ibanking.unitybank.com.au/OpenBanking/cds-au/v1
Unloan: https://public.api.cdr.unloan.com.au/cds-au/v1
Up: https://api.up.com.au/cds-au/v1
Virgin Money: https://api.cds.virginmoney.com.au/cds-au/v1
Westpac: https://digital-api.westpac.com.au/cds-au/v1
Wise: https://au-cdrbanking-pub.wise.com/cds-au/v1
Woolworths Team Bank: https://online.woolworthsteambank.com.au/OpenBanking/cds-au/v1
bankWAW: https://onlinebanking.wawcu.com.au/OpenBanking/cds-au/v1
gmcu: https://secure.gmcu.com.au/OpenBanking/cds-au/v1
in1bank ltd.: https://cdr.in1bank.com.au/cds-au/v1
```
<!-- /BRANDS -->

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
