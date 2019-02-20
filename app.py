from flask import Flask, render_template, request, redirect, url_for
import httplib2
import json
import requests


app = Flask(__name__)

# Show all 
@app.route('/')
def show():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)