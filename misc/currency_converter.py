import requests
from bs4 import BeautifulSoup as bs


class Currency:
    def get_converted_currency(self, src, dest, amount=1):
        content = requests.get(f"https://www.x-rates.com/table/?from={src}&amount={amount}").content
        soup = bs(content, "html.parser")
        exchange_tables = soup.find_all("table")
        exchange_rates = {}
        for exchange_table in exchange_tables:
            for tr in exchange_table.find_all("tr"):
                tds = tr.find_all("td")
                if tds:
                    currency = tds[0].text
                    exchange_rate = float(tds[1].text)
                    exchange_rates[currency] = exchange_rate        
        
        return exchange_rates[dest]


# cur = Currency()
# print(cur.get_converted_currency('USD', 'ILS'))


import json 

import requests 

  
# defining key/request url 

key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

  
# requesting data from url 

data = requests.get(key)   

data = data.json() 

print(f"{data['symbol']} price is {data['price']}")