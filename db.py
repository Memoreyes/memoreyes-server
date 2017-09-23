import json

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


dataObject = read_user_data('123456')
print(dataObject)
#print(json.dumps(dataObject, indent=2, separators=(',', ': ')))
