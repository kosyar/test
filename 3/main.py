# -*- coding: utf-8 -*-
import asyncio
import requests
city = ["yaroslavl", "moscow","london"]


def humanReadDataConvetor(json):
    pass


async def getWeather(city):
    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=%s&lang=ru&appid=8d5f992c262591bad03eb29d23d002f6&units=metric" % city)
    if (r.status_code == 200):
        # print(r.headers['Content-Type'])
        # print(r.json())
        rep = r.json()
        new_file = open("%s.txt" % city, mode="w", encoding="utf-8")
        new_file.write(r.text)
        new_file.close()
        # print(type(rep))
        new_file = open("HumanRead_%s.txt" % city, mode="w", encoding="utf-8")
        new_file.write("Город:" + rep['name']+ "\n")
        new_file.write("Осадки:"+ rep['weather'][0]['description']+ "\n")
        new_file.write("Температура:" + str(rep['main']['temp'])+ "\n")
        new_file.write("Цуствуется как:"+ str(rep['main']['feels_like'])+ "\n")
        new_file.write("Ветер:"+ str(rep['wind']['speed'])+ "\n")
        new_file.close()
    await asyncio.sleep(1)
    print("%s Done!"%city)


ioloop = asyncio.get_event_loop()
tasks = [
]
for i in city:
    tasks.append(ioloop.create_task(getWeather(i)))
ioloop.run_until_complete(asyncio.wait(tasks))
print("exit")

ioloop.close()
