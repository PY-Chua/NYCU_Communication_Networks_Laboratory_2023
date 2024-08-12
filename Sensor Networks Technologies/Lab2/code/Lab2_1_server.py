# -*- coding: utf-8 -*-
import os
import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:1234")

print('Worker %s is running ...' % os.getpid())

while True:
    # Receive a, b from the client
    # ?????? function
    #   1. socket.recv_multipart()
    ''' start of you code '''
    a, b = socket.recv_multipart()
    a = int(a.decode('UTF-8'))
    b = int(b.decode('UTF-8'))
    ''' end of you code '''

    # Return the result back to the client
    # ?????? function
    #   1. socket.send_string(....)
    ''' start of you code '''
    print( 'Compute %s + %s and response' % (a, b) )
    socket.send_string(str(a + b) + "(from worker "+ str(os.getpid()) +")" )
    ''' end of you code '''