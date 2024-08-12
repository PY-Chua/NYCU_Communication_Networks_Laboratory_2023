import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

TRIG = 16
E = 18
LED_PIN = 12

print '1'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(E, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)

# Setup DHT11 
sensor_args = {'11' : Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
sensor = sensor_args['11']

# GPIO#, ex: GPIO4 = Pin7
gpio = 4

	
def temperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temperature is not None:
        return temperature
    else:
        print('Failed to get reading. Try again!')
        return

def measure():
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(TRIG, GPIO.LOW)
    pulse_start = 0
    pulse_end = 0
    while GPIO.input(E) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(E) == GPIO.HIGH:
        pulse_end = time.time()
    t = pulse_end - pulse_start
    temp = temperature()
    v = 331 + 0.6 * temp
    d = t * v
    d = d / 2
    print("=============================")
    print('Temp: {0:0.1f}*C'.format(temp))
    print('V = 331 + 0.6 * {0:0.1f}'.format(temp))
    print('  = {0:0.1f}'.format(v))
    return d * 100

while(1):
    distance = measure()
    print('Distance: {0:0.1f}cm'.format(distance))
    
    if distance < 10:
        print("Distance < 10")
        GPIO.output(LED_PIN, GPIO.HIGH)
    elif distance >= 10 and distance <= 20:
        print("10 < Distance < 20")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1)
    elif distance > 20:
        print("Distance > 20")
        GPIO.output(LED_PIN, GPIO.LOW)
    
    time.sleep(1)
GPIO.cleanup()