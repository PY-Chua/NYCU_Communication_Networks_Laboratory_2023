# -*- coding: utf-8 -*-
from flask import Flask, request, Response, jsonify, make_response

from flask_restful import Api
from flask_restful import Resource

import Adafruit_DHT

# Setup DHT11 
sensor_args = {'11' : Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
sensor = sensor_args['11']

# GPIO#, ex: GPIO4 = Pin7
gpio = 4

class MyApp(Resource):
    def get(self):
        return Response(
            '''
            Welcome to my humidity&temperature RESTful API.
            Please make a HTTP POST request to this app, and you can
            decide to get the humidity or temperature data.
            The json embedded in the request woudl be:

            {
                "user" : "109511286",
                "data" : "H"
            }

            or

            {
                "user" : "109511286",
                "data" : "T"
            }
            '''
        )
    
    def post(self):
        json = request.get_json()

        if len(json) == 0:
            # ??????? Json ?????,??? HTTP Status Code = 400 ?????
            # ?????? functions
            #    1. jsonify(message = ....)
            #    2. make_response(...., 400)

            ''' start of you code '''
            return make_response(jsonify({'message':'Status Code = 400'}), 400)
            
            
            ''' end of you code '''
        
        ID = str(json['user'])
        data_type = json['data']


        # ??????????
        # ?????? function
        #    1.  Adafruit_DHT.read_retry(...., ....)
 
        ''' start of you code '''
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
        h = str(humidity)
        t = str(temperature)
        
        
        ''' end of you code '''
   
        # ? json field "data" ????????????????,??????(else ???)
        # ?????? functions
        #    1. jsonify(message = ....)
        #    2. make_response(...., 200) or make_response(...., 400) (else ??) 
        #
        ''' start of you code '''
    
    
    
        ''' end of you code '''
        
        if data_type == 'T':
            ''' start of you code '''
            str1='Hi, '+ID+' the current temperature is '+t+' C'
            return make_response(jsonify({'message':str1}), 200)
            
            
            ''' end of you code '''
        
        elif data_type == 'H':
            ''' start of you code '''
            str2='Hi, '+ID+' the current humidity is '+h+' %'
            return make_response(jsonify({'message':str2}), 200)
            
            
            ''' end of you code '''
        
        else:
            ''' start of you code '''
            return make_response(jsonify({'message':'Status Code = 400'}), 400)
            
            
            ''' end of you code '''

app = Flask(__name__)      
api = Api(app)

api.add_resource(MyApp, '/')

if __name__ == '__main__':
    app.run(host = '192.168.230.150', port = 9808, debug = True)