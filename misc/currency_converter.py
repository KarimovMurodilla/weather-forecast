import aiohttp
import asyncio
from bs4 import BeautifulSoup as bs


class Currency:
    async def convert(self, from_currency, to_currency, amount=1):
        async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.get('https://api.exchangerate-api.com/v4/latest/USD') as response:
                data = await response.json()
        currencies = data['rates']
        # first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD':
            amount = amount / currencies[from_currency]
        # limiting the precision to 4 decimal places
        amount = round(amount * currencies[to_currency], 2)
        return amount


class CryptoCurrency:
    async def create_link(self, name):
        link = f"https://coincodex.com/api/coincodex/get_coin/{name}"
        return link

    async def get_response_data(self, key) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(key) as response:
                data = await response.json()
        return data

    async def get_btc(self):
        key = await self.create_link('BTC')
        result = await self.get_response_data(key)
        return round(result['today_open'], 1)

    async def get_eth(self):
        key = await self.create_link('ETH')
        result = await self.get_response_data(key)
        return round(result['today_open'], 1)

    async def get_ton(self):
        key = "https://coincodex.com/api/coincodex/get_coin/toncoin"
        result = await self.get_response_data(key)
        return round(result['today_open'], 1)


class CurrencyMixins(Currency, CryptoCurrency):
    """This class inherits from classes that include the currencies and cryptocurrencies"""
