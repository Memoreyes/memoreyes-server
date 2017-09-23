from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return 'Welcome to Memoreyes</br>'+time

@app.route('/api')
def api():
    return 'API'
