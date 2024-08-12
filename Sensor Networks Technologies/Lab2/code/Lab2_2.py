# -*- coding: utf-8 -*-
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
# IP ????
socket.connect("tcp://192.168.50.34:5556")
# 

# Subscribe to two topics, humidity and temp
# ?????? function
#   1. socket.setsockopt(zmq.SUBSCRIBE, ....)
''' start of you code '''
topicfilter1 = "humidity"
topicfilter2 = "temp"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter1)
socket.setsockopt(zmq.SUBSCRIBE, topicfilter2)
''' end of you code '''

print("Start!!\n")

temp_sum = 0
humid_sum = 0

for i in range(10):
    # receive temperature from TA 
    # ???? mes string ???,???????,split ???? string list
    # ?????? function
    #   1. socket.recv()
    #   2. string.split
    ''' start of you code '''
    mes = socket.recv()
    print(mes)
    splitted_str = mes.split()
    for word in splitted_str:
        if word.isdigit():
            temp_sum += int(word)
    ''' end of you code '''

    # receive humidity from TA 
    # ???? mes string ???,???????,split ???? string list
    # ?????? function
    #   1. socket.recv()
    #   2. string.split
    ''' start of you code '''
    mes = socket.recv()
    print(mes)
    splitted_str = mes.split()
    for word in splitted_str:
        if word.isdigit():
            humid_sum += int(word)
    ''' end of you code '''

# Compute average value
print("avg temperature: {}".format(temp_sum / 10.0))
print("avg humidity: {}".format(humid_sum / 10.0))