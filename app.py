from flask import Flask ,jsonify
from data import books_data
app = Flask(__name__)
print(__name__)

@app.route('/')
def helloWorld():
    return jsonify({'books': books_data})

app.run(port=5000)