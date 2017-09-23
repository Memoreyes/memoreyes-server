from flask import Flask
from flask import request
import datetime, json
import os
app = Flask(__name__)

@app.route('/', methods=['POST'])
def api():
    time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    requestingUserId = request.form['userId']
    f = request.files['photo']
    f.save('/root/memoreyes-server/uploaded_image.jpg')
    return json.dumps({'success':'true','time':time})

# returns a complete set of data for a given user
def read_user_data(userId):
    with open(userId+'.json', 'r') as dataFile:
        data = json.load(dataFile)
        return data

# writes a full set of data for a given user
def write_user_data(userId, newData):
    with open(userId+'.json', 'w') as dataFile:
        json.dump(newData, dataFile)
        return True

# adds a person to a user's data set
def add_person(userId, personsName, personsRelationship):
    data = read_user_data(userId)
    data['people'][personsName] = personsRelationship
    write_user_data(userId, data)
    return True

# checks to see if a person is in a user's data set by name
def check_for_person(userId, personsName):
    data = read_user_data(userId)
    if personsName in data['people']:
        return True

# adds a drug to a user's data set
def add_drug(userId, drugName, drugInstructions):
    data = read_user_data(userId)
    data['drugs'][drugName] = drugInstructions
    write_user_data(userId, data)
    return True

# checks to see if a drug is in a user's data set by name
def check_for_drug(userId, drugName):
    data = read_user_data(userId)
    if drugName in data['drugs']:
        return True

# Debug DB
    # dataObject = read_user_data('123456')
    # print(json.dumps(dataObject, indent=2, separators=(',', ': ')))

def speak_name(personsName):
	with open('DATA.txt','w') as dataFile:
		json.dump(personsName, dataFile)
	os.system('node texttospeechv1.js')


