from discord.ext import commands
from datetime import datetime
from bs4 import BeautifulSoup
from Data import save
import requests

async def pollution(message):
    response1 = requests.get("https://airnow.tehran.ir/")
    result1 = BeautifulSoup(response.text, "html.parser")

    today = result1.find("span", {"id" : "ContentPlaceHolder1_lblAqi3h"}).get_text()
    today = int(today)
    yesterday = result1.find("span", {"id" : "ContentPlaceHolder1_lblAqi24h"}).get_text()

    if (int(today) > int(yesterday)):
        res = "These days are not in good condition"
        await message.reply(f'''
            :page_with_curl: Today's pollution is : {today}

:weary: Result : {res}
            ''')
    else:
        res = "These days are going to be better"
        await message.reply(f'''
            :page_with_curl: Today's pollution is : {today}

:heart_eyes: Result : {res}
            ''')

    response2 = requests.get("https://www.tomorrow.io/weather/")
    result2 = BeautifulSoup(response2.text, "html.parser")
    temp = result2.find("span", {"class" : "_3fQrr5"}).get_text()
    final_result = ""
    for i in temp:
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if (i in numbers):
            final_result += i

    final_result = int(final_result)
    save(message, today, final_result)


async def temperature(message):
    response1 = requests.get("https://www.tomorrow.io/weather/")
    result1 = BeautifulSoup(response1.text, "html.parser")
    temp = result1.find("span", {"class" : "_3fQrr5"}).get_text()
    final_result = ""
    for i in temp:
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if (i in numbers):
            final_result += i

    final_result = int(final_result)
    if (final_result >= 28):
        await message.reply(f":melting_face: The temperature is {final_result}°C")

    if (10 <= final_result <= 27):
        await message.reply(f":grinning: The temperature is {final_result}°C")

    if (0 <= final_result <= 9):
        await message.reply(f":grimacing: The temperature is {final_result}°C")

    if (final_result <= -1):
        await message.reply(f":cold_face: The temperature is {final_result}°C")


    response2 = requests.get("https://airnow.tehran.ir/")
    result2 = BeautifulSoup(response2.text, "html.parser")

    today = result2.find("span", {"id" : "ContentPlaceHolder1_lblAqi3h"}).get_text()
    today = int(today)

    save(message, today, final_result)