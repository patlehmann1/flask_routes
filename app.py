from flask import Flask, escape, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/name/<name>')
def hello_user(name):
    return 'Hello, %s' % escape(name)

@app.route('/square_a_number/<int:number>')
def square_a_number(number):
    squared = number**2
    return f'{number} squared is {squared}'