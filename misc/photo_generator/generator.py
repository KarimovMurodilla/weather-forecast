from locale import currency
from PIL import Image, ImageDraw, ImageFont
from loader import owm, cur

class PhotoGenerator:
    def __init__(self):
        self.img_path = 'misc/photo_generator/img/israely.jpg'
        self.font_path = 'misc/photo_generator/fonts/arial.ttf'
        self.font_path2 = 'misc/photo_generator/fonts/calibri.ttf'
        self.save_path = "misc/photo_generator/img/image_text.jpg"
    

    def get_photo_coords_for_weather(self):
        # Weather
        weather = [
            (1497, 1140), (2300, 1140), (3160, 1140),
            (1497, 1360), (2300, 1360), (3160, 1360),
            (1497, 1580), (2300, 1580), (3160, 1580),
            (1497, 1790), (2300, 1790), (3160, 1790),
            (1497, 2010), (2300, 2010), (3160, 2010),
            (1497, 2220), (2300, 2220), (3160, 2220),
            (1497, 2440), (2300, 2440), (3160, 2440),
            (1497, 2650), (2300, 2650), (3160, 2650)
        ]

        # Currencies
        currencies = [ 
            (1505, 3090),
            (1505, 3300),
            (1505, 3500),

            (2457, 3100),
            (2457, 3300),
            (2457, 3500)
        ]

        coords = [weather, currencies]

        return coords
    

    def get_places(self):
        places = [
            'Tel-Aviv', 
            'Jerusalem', 
            'Ashkelon', 
            'Ashdod', 
            'Netanya', 
            'Haifa', 
            'Tiberias', 
            'Safed'
        ]

        return places
    

    def get_list_currency(self):
        curs = [
            "USD",
            "RUB",
            "UAH"
        ]
        return curs
    

    def get_all_info_list(self):
        places = self.get_places()
        curs = self.get_list_currency()
        winfo = []

        currency_info = []
        
        for p in places:
            weather = owm.get_weather_info(p)
            winfo.append(weather.celsius)
            winfo.append(weather.wind_speed)
            winfo.append(weather.humidity)
        
        for c in curs:
            res = cur.convert(c, "ILS")
            currency_info.append(res)

        currency_info.append(cur.get_btc())
        currency_info.append(cur.get_eth())
        currency_info.append(cur.get_ton())

        all_data = [winfo, currency_info]

        return all_data


    def put_weather_info_on_photo(self):
        coords = self.get_photo_coords_for_weather()
        all_data = self.get_all_info_list()

        with Image.open(self.img_path) as img:
            d1 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype(self.font_path, 100)

            for coord, win in zip(coords[0], all_data[0]):
                d1.text((coord[0], coord[1]), str(win), font=myFont, fill=(0, 0, 0))
            
            myFont = ImageFont.truetype(self.font_path2, 100)
            for coord, win in zip(coords[1], all_data[1]):
                d1.text((coord[0], coord[1]), str(win), font=myFont, fill=(255, 255, 255))

            img.save(self.save_path)