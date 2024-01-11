import Adafruit_DHT
import time
import datetime
import asyncio
import aiofiles as aiof

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 2

humidity = 0
temperature = 0

async def update_dht():
    global humidity
    global temperature
    while True:
        new_humidity, new_temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if new_humidity is not None and new_temperature is not None:
            humidity = new_humidity
            temperature = new_temperature
        await asyncio.sleep(3)

async def print_data():
    with open('data.csv', 'w') as data_file:
        data_file.write('time;temperature;humidity\n')
        while True:
            print("{}: Temperature={:0.1f}C Huimidity={:0.1f}%".format(datetime.datetime.now(), temperature, humidity))
            data_file.write('{};{:0.1f};{:0.1f}\n'.format(datetime.datetime.now(), temperature, humidity))
            data_file.flush()
            await asyncio.sleep(60)
    
async def main():
    update_task = asyncio.create_task(update_dht())
    time.sleep(5)
    print_task = asyncio.create_task(print_data())
    await update_task
    await print_task
    
asyncio.run(main())