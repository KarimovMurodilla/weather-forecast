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



  
class CryptoCurrency:
    def __init__(self):
        self.btc = None
        self.eth = None
    

    def create_link(self, name):
        link = f"https://api.binance.com/api/v3/ticker/price?symbol={name}USDT"
        return link

    
    def get_response_data(self, key) -> dict:
        data = requests.get(key)   
        data = data.json()

        return data
    

    def get_btc(self):
        key = self.create_link('BTC')
        result = self.get_response_data(key)

        return result.get('price')
    

    def get_eth(self):
        key = self.create_link('ETH')
        result = self.get_response_data(key)

        return result.get('price')
    

    def get_ton(self):
        key = "https://coincodex.com/api/coincodex/get_coin/toncoin"
        data = requests.get(key)   
        data = data.json()

        return round(data['today_open'], 3)


c = CryptoCurrency()
res = c.get_ton()
print(res)