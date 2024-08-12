# -*- coding: utf-8 -*-
import zmq
import random
import time

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.bind("tcp://*:1234")

# wait for all workers connected
time.sleep(1)

for i in range(9):
    a = str(random.randint(0, 100))
    b = str(random.randint(0, 100))
    
    # Send integer a, b to servers
    # ?????? functions
    #   1. socket.send_multipart
    ''' start of you code '''
    print( 'Compute %s + %s' % (a, b) )
    socket.send_multipart([bytes(a.encode('UTF-8')), bytes(b.encode('UTF-8'))])
    ''' end of you code '''
    
    # receive results from servers
    # ?????? function
    #   1. socket.recv()
    ''' start of you code '''
    c = socket.recv()
    print( ' = ' + c.decode('UTF-8') )
    ''' end of you code '''
    