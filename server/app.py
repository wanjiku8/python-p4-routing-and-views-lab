#!/usr/bin/env python3
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to print a string
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter) 
    return parameter 

# Route to count numbers
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(num) for num in range(parameter))
    return numbers

# Route for math operations
@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400 
    
    return str(result)

# Run the application if this file is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)