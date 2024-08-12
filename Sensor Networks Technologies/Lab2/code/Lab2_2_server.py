# -*- coding: utf-8 -*-
import zmq
import random
import time

import Adafruit_DHT

# Setup DHT11 
sensor_args = {'11' : Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
sensor = sensor_args['11']

# GPIO#, ex: GPIO4 = Pin7
gpio = 4

context = zmq.Context()
socket = context.socket(zmq.PUB)

# IP ????
socket.bind("tcp://192.168.230.150:5556")


while True:
    # ??????????
    # ?????? function
    #    1.  Adafruit_DHT.read_retry(...., ....)

    ''' start of you code '''
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    humidity = int(humidity)
    temp = int(temperature)
    ''' end of you code '''

    socket.send("temp = %d" % (temp))
    time.sleep(0.5)

    socket.send("humidity = %d" % (humidity))
    time.sleep(0.5)