from flask import Flask
from flask import request
import datetime, json
app = Flask(__name__)

@app.route('/')
def index():
    time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return 'Welcome to Memoreyes</br>'+time

@app.route('/api', methods=['GET','POST'])
def api():
    if request.method == 'POST':
        return parse_request()
    if request.method == 'GET':
        return return_request()
    else:
        abort(401)
        return 'ERROR'

def parse_request():
    return "Y U SEND POST"

def return_request():
    time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return json.dumps({'success':'true','time':time})

# request.args.get('key', '')

# request.form['username']

# f = request.files['the_file']
# f.save('/var/www/uploads/uploaded_file.txt')
