# from misc.currency_converter import CurrencyMixins
# from misc.owm import Owm
# from misc.photo_generator.generator import PhotoGenerator
# from app.config import API_KEY

# owm = Owm(API_KEY)

# weather = owm.get_weather_info('Jerusalem')
# print(weather.celsius)
# print(weather.wind_speed)
# print(weather.humidity)


# Currency
# cur = CurrencyMixins()
# print(cur.get_btc())
# print(cur.get_eth())
# print(cur.get_ton())
# curs = [
#     "USD",
#     "RUB",
#     "UAH"
# ]

# for c in curs:
#     res = cur.convert(c, "ILS")
#     print(res)


# coords = [
#     (1497, 1140), (2300, 1140), (3160, 1140),
#     (1497, 1360), (2300, 1360), (3160, 1360),
#     (1497, 1580), (2300, 1580), (3160, 1580),
#     (1497, 1790), (2300, 1790), (3160, 1790),
#     (1497, 2010), (2300, 2010), (3160, 2010),
#     (1497, 2220), (2300, 2220), (3160, 2220),
#     (1497, 2440), (2300, 2440), (3160, 2440),
#     (1497, 2650), (2300, 2650), (3160, 2650)
# ]

# places = [
#     'Tel-Aviv', 
#     'Jerusalem', 
#     'Ashkelon', 
#     'Ashdod', 
#     'Netanya', 
#     'Haifa', 
#     'Tiberias', 
#     'Safed'
# ]

# winfo = []
# for p in places:
#     weather = owm.get_weather_info(p)
#     winfo.append(weather.celsius)
#     winfo.append(weather.wind_speed)
#     winfo.append(weather.humidity)


# g = PhotoGenerator()
# g.put_weather_info_on_photo()