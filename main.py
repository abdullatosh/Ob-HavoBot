import requests
import telebot
import json
token = 'TOKEN'

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start(massage):
    bot.send_message(massage.chat.id , 'Ob-Havo malumotlarini bilish uchun shahringizni nomini kiriting: ')

@bot.message_handler(content_types = ['text'])
def obHavo(massage):
    api_url = 'https://api.openweathermap.org/data/2.5/weather'
    city = massage.text
    r = requests.post(url = api_url, params ={'q': city, 'APPID' : #Bu yerga openweatherdan oldan API key kitirladi, 'units' : 'metric' })
    if r.status_code  == 200:

        response = json.loads(r.content)
        temp = str(response['main']['temp'])
        max_temp = str(response['main']['temp_max'])
        min_temp = str(response['main']['temp_min'])
        wind_speed = str(response['wind']['speed'])
        pressure = str(response['main']['pressure'])
        humidity = str(response['main']['humidity'])

        msg = '🌍 ' + city +  ' : ' + temp + '°C' + '\n' + '🌡 Yuqori harorat : ' + max_temp + '°C' + '\n' + '🌡 Past harorat : ' + min_temp + '°C' + '\n' + '🌪 Shamol tezligi : ' + wind_speed + 'm/s' + '\n' + '⏱ Havo bosimi : ' + pressure + '\n' + '💧 Nisbiy namlik : ' + humidity + '%'

        bot.send_message(massage.chat.id , msg)
    else:
        bot.send_message(massage.chat.id, "Shahar nomi noto\'g\'ri")

bot.polling(none_stop=True)