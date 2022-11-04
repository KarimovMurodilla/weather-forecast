import requests
from bs4 import BeautifulSoup as bs


class Currency:
    def __init__(self):
        self.data= requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
        self.currencies = self.data['rates']
    

    def convert(self, from_currency, to_currency, amount = 1): 
        initial_amount = amount 
        #first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 
    
        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency], 2) 
        return amount
        
  
class CryptoCurrency:  
    def create_link(self, name):
        link = f"https://coincodex.com/api/coincodex/get_coin/{name}"
        return link

    
    def get_response_data(self, key) -> dict:
        data = requests.get(key)   
        data = data.json()

        return data
    

    def get_btc(self):
        key = self.create_link('BTC')
        result = self.get_response_data(key)

        return round(result['today_open'], 1)
    

    def get_eth(self):
        key = self.create_link('ETH')
        result = self.get_response_data(key)

        return round(result['today_open'], 1)
    

    def get_ton(self):
        key = "https://coincodex.com/api/coincodex/get_coin/toncoin"
        result = self.get_response_data(key)

        return round(result['today_open'], 1)


class CurrencyMixins(Currency, CryptoCurrency):
    """This class inherits from classes that include the currencies and cryptocurrencies"""