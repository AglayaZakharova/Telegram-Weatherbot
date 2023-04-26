# -*- coding: utf-8 -*-
from config import open_weather_token
import requests
import datetime


def show_weather(city, open_weather_token):
    emoji_codes = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    try:
        s = 'http://api.openweathermap.org/data/2.5/weather'
        rec_params = {
            "q": city,
            "appid": open_weather_token,
            "units": 'metric'
        }
        response = requests.get(s, rec_params)
        data = response.json()

        city = data["name"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]

        sky = data["weather"][0]["main"]
        if sky in emoji_codes:
            wd = emoji_codes[sky]
        else:
            wd = "Посмотри сам! Никак не разберу, что там за погода..."

        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        wind_speed = data["wind"]["speed"]
        wind_gust = data["wind"]["gust"]

        sunrise_time = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_time = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        day_length = sunset_time - sunrise_time

        print(f"*** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ***\n"
                                        f"\nПогода в городе: {city}\nТемпература: {temp}°C, "
                                        f"ощущается как {feels_like}°C.\n"
                                        f"За окном: {wd}\n"
                                        f"\nДавление: {pressure} мм.рт.ст.\n"
                                        f"Влажность: {humidity}%.\n"
                                        f"Ветер {wind_speed}м/с с порывами до {wind_gust}м/с.\n"
                                        f"\nДиапазон температур в этот день: {temp_min}-{temp_max}°C.\n"
                                        f"Время восхода: {sunrise_time.strftime('%H:%M')}.\n"
                                        f"Время заката: {sunset_time.strftime('%H:%M')}.\n"
                                        f"Продолжительность светового дня: {day_length}."
                                        f"\nХорошего дня! :)")
    except:
        print('Что-то не выходит. Пожалуйста, проверьте название города.')


def main():
    city = input()
    show_weather(city, open_weather_token)


if __name__ == '__main__':
    main()