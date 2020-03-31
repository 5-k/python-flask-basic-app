from flask import Flask ,jsonify

app = Flask(__name__)
print(__name__)

books = [
        {
            'name' : 'MS Azure Training',
            'price' : 22.34,
            'purchased_date' : '22-02-2019'
        }, {
            'name' : 'My Dictionary',
            'price' : 233.1,
            'purchased_date' : '02-09-2019'
        }
    ]
@app.route('/')
def helloWorld():
    return jsonify({'books': books})

app.run(port=5000)