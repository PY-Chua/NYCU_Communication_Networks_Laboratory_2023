import RPi.GPIO as GPIO
import time
import sys, select
import socket

GPIO.setwarnings(False)

v = 343
TRIG = 16
E = 18

print '1'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(E, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)
HOST = '192.168.185.42'
PORT = 2000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


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
    d = t * v
    d = d / 2
    return d * 100

while(1):
    i, o, e = select.select([sys.stdin], [], [], 3)
    if(i):
        a = sys.stdin.readline().strip()
        client.sendall(a)
        print(a, type(a))
    else:
        print("Nothing")
    distance = measure()
    print(distance)

    if distance < 10:
        print("Distance < 10")
        client.sendall('s')
    time.sleep(1)
GPIO.cleanup()

'''
import RPi.GPIO as GPIO
import time
import sys, select
import socket

GPIO.setwarnings(False)

v = 343
TRIG = 16
E = 18
#LED_PIN = 12

print '1'
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(E, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)
HOST = '192.168.185.42'
PORT = 2000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


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
    d = t * v
    d = d / 2
    return d * 100

while(1):
    i, o, e = select.select([sys.stdin], [], [], 3)
    user_input = input("Input w, a, s, d, x: ")
    if(i):
        a = sys.stdin.readline().strip()
        client.sendall(a)
        print(a, type(a))
    else:
        print("Nothing")
    distance = measure()
    print(distance)

    if distance < 10:
        print("Distance < 10")
        #GPIO.output(LED_PIN, GPIO.HIGH)
        client.sendall("s")
    # elif distance >= 10 and distance <= 20:
    #     print("10 < Distance < 20")
    #     GPIO.output(LED_PIN, GPIO.HIGH)
    #     time.sleep(0.1)
    #     GPIO.output(LED_PIN, GPIO.LOW)
    #     time.sleep(0.1)
    # elif distance > 20:
    #     print("Distance > 20")
    #     GPIO.output(LED_PIN, GPIO.LOW)
    
    if user_input == 'w':
        # Send forward command to the server
        client.sendall("w")
    elif user_input == 'x':
        # Send backward command to the server
        client.sendall("x")
    elif user_input == 'a':
        # Send left turn command to the server
        client.sendall("a")
    elif user_input == 'd':
        # Send right turn command to the server
        client.sendall("d")
    elif user_input == 's':
        # Self input stop
        client.sendall("s")
    
    time.sleep(0.1)
GPIO.cleanup()
'''