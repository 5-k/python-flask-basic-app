from flask import Flask,jsonify, request
from validation import *
from data import books_data
from service import *

prateekApp = Flask(__name__)

books = books_data

@prateekApp.route('/<int:id>', methods=['GET'])
def testIfInputRecievedIsCorrect(id):
    return jsonify(id)

@prateekApp.route('/book', methods=['GET'])
def getAllBooks():
    return jsonify(books)

@prateekApp.route('/book/<int:id>', methods=['GET'])
def getSpecificBook(id):
    for data in books:
        print(data)
        if (data['id'] == id):
            return jsonify(data)

    return jsonify(None)

@prateekApp.route('/book', methods=['POST'])
def createNewBook():
    input = request.get_json() 
    if not validateIfDataHasRequiredFields(input):
        return jsonify({'Error': 'Missing required fields'})
    elif validateIfNameAlreadyAdded(input):
        return jsonify({'Error':'This Book is already added'})

    id = GetNewId()
    
    santized_input = getValidBook(input)
    santized_input['id'] = id
    books_data.append(santized_input)
    return jsonify({'Message' : 'Added book with id: ' + str(id) })


prateekApp.run(port=5000)