import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) 

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

# Setup DHT11 
sensor_args = {'11' : Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
sensor = sensor_args['11']

# GPIO#, ex: GPIO4 = Pin7
gpio = 4

user_input = input()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}* Humidity={1:0.1f}%'.format(temperature, humidity))
        if temperature > user_input:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
        
GPIO.cleanup()