# -*- coding: utf-8 -*-
import time

import RPi.GPIO as GPIO

import telepot
from telepot.loop import MessageLoop

import Adafruit_DHT

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# LED_1_PIN 
''' start of you code '''
PIN = 11                                    
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, False) 
''' end of you code '''

# Setup DHT11 
''' start of you code '''
sensor_args = {'11' : Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
sensor = sensor_args['11']
''' end of you code '''

# GPIO#, ex: GPIO4 = Pin7
''' start of you code '''
gpio = 4
''' end of you code '''

def action(msg):
    # ??? Telegram Bot ?????,?? chat_id ? text
    # msg ? nested dict 
    # ?????? function
    #   1. msg['...']
    ''' start of you code '''
    chat_id = msg['chat']['id']
    command = msg['text'] 

    print('Received: {cmd}'.format(cmd = command))
    ''' end of you code '''

    # ??????????? LED ?
    # ?????? function
    #    1. GPIO.output(..., ...)
    #    2. telegram_bot.sendMessage(chat_id, message)

    ''' start of you code '''
    if command == '/ledon':
        GPIO.output(PIN, True)
        telegram_bot.sendMessage(chat_id, "Turned on the light")

    elif command == '/ledoff':
        GPIO.output(PIN, False)
        telegram_bot.sendMessage(chat_id, "Turned off the light")

    ''' end of you code '''

    # Get humidity & temperature
    # ?????? function
    #    1.  Adafruit_DHT.read_retry(...., ....)
    ''' start of you code '''
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    humidity = float(humidity)
    temperature = float(temperature)
    ''' end of you code '''

    # ??????????? Telegram Bot ?????????
    # ?????? function
    #    1. telegram_bot.sendMessage(chat_id, message)
    ''' start of you code '''
    if command == '/humid':
        telegram_bot.sendMessage(chat_id, "The current humidity is {h:.1f} %".format(h = humidity))
        print('The current humidity is {h:.1f} %'.format(h = humidity))

    elif command == '/temp':
        telegram_bot.sendMessage(chat_id, "The current temperature is {t:.1f} *C".format(t=temperature))
        print('The current temperature is {t:.1f} *C'.format(t=temperature))
    ''' end of you code '''

# ?????? Telegram Bot ? token
''' start of you code '''
telegram_bot = telepot.Bot('6698550633:AAG-leIe25N9nax0SrfgF73qPScQSFIXkvI')
''' end of you code '''

print(telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print('Send the command to turn on or off the light...')

while True:
    time.sleep(3)