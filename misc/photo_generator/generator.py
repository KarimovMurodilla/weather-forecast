from PIL import Image, ImageDraw, ImageFont
from loader import owm, cur

class PhotoGenerator:
    def __init__(self):
        self.img_path = 'misc/photo_generator/img/israely.jpg'
        self.font_path = 'misc/photo_generator/fonts/arial.ttf'
        self.font_path2 = 'misc/photo_generator/fonts/calibri.ttf'
        self.saved_path = "misc/photo_generator/img/image_text.jpg"
    

    async def get_photo_coords_for_weather(self):
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
    

    async def get_places(self):
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
    

    async def get_list_currency(self):
        curs = [
            "USD",
            "RUB",
            "UAH"
        ]
        return curs
    

    async def get_all_info_list(self):
        places = await self.get_places()
        curs = await self.get_list_currency()
        winfo = []

        currency_info = []
        
        for p in places:
            weather = await owm.get_weather_info(p)
            winfo.append(weather.celsius)
            winfo.append(weather.wind_speed)
            winfo.append(weather.humidity)
        
        for c in curs:
            if c == 'USD':
                res = await cur.convert(c, "ILS")
            else:
                res = await cur.convert('ILS', c)
            currency_info.append(res)

        currency_info.append(await cur.get_btc())
        currency_info.append(await cur.get_eth())
        currency_info.append(await cur.get_ton())

        all_data = [winfo, currency_info]

        return all_data


    async def put_all_info_on_photo(self):
        coords = await self.get_photo_coords_for_weather()
        all_data = await self.get_all_info_list()

        with Image.open(self.img_path) as img:
            d1 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype(self.font_path, 100)

            for coord, win in zip(coords[0], all_data[0]):
                d1.text((coord[0], coord[1]), str(win), font=myFont, fill=(0, 0, 0))
            
            myFont = ImageFont.truetype(self.font_path2, 100)
            for coord, win in zip(coords[1], all_data[1]):
                d1.text((coord[0], coord[1]), str(win), font=myFont, fill=(255, 255, 255))

            img.save(self.saved_path)
        
        return self.saved_path