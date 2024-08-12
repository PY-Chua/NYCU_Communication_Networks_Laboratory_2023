# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    # S
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.3)
    # O
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.3)
    # S
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.7)

GPIO.cleanup()