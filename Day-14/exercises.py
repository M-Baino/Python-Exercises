# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:21:54 2019

@author: Muath
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello(user):
    return '<html><body><h1>This is the Index page</h1></body></html>'

@app.route('/hello')
def hello2(user):
    return '<html><body><h1>Hello World!</h1></body></html>'

@app.route('/members')
def hello3(user):
    return '<html><body><h1>Members Page</h1></body></html>'


