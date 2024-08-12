# -*- coding: utf-8 -*-
import lirc
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# LED_1_PIN 
PIN = 11                                   
GPIO.setup(PIN, GPIO.OUT)

# LED_2_PIN 
PIN_2 = 13                                 
GPIO.setup(PIN_2, GPIO.OUT)

sockid = lirc.init('LED', '.lircrc', verbose = True)

while True:
    inf = lirc.nextcode()

    if len(inf) == 0:
        continue
    
    # 判斷 inf[0] 的值是與自己在 .lircrc 檔案中所設定的哪個 key 相符
    # 判斷後再決定對 LED 進行亮暗控制
    # 會用到的 function
    #   1. GPIO.output(PIN, ....)
    ''' start of you code '''
    if inf[0]=='LED_1_ON':
        GPIO.output(PIN, GPIO.HIGH)
    elif inf[0] == 'LED_2_ON':
        GPIO.output(PIN_2, GPIO.HIGH)
    elif inf[0] == 'LED_1_OFF':
        GPIO.output(PIN, GPIO.LOW)
    elif inf[0] == 'LED_2_OFF':
        GPIO.output(PIN_2, GPIO.LOW)
    ''' end of you code '''

lirc.deinit()
