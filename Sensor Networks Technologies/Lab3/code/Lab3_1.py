# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def index():
    # ?????? function
    #   1. render_template('index.html', ID = ....)
    ''' start of you code '''
    return render_template('index.html', ID = '109511286') 
    ''' end of you code '''
    
@app.route('/pages')
def pages():
    return render_template('index.html', ID = '109511286')
    
if __name__ == '__main__':
    app.run(host = '192.168.105.150', port = 9808, debug = False)