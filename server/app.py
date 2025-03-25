#!/usr/bin/env python3
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    """Home page that displays a heading"""
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to print a string
@app.route('/print/<string:parameter>')
def print_string(parameter):
    """Prints the parameter to console and returns it to the browser"""
    print(parameter)  # This shows in your terminal/command prompt
    return parameter  # This shows in your web browser

# Route to count numbers
@app.route('/count/<int:parameter>')
def count(parameter):
    """Displays numbers from 0 to parameter-1, each on a new line"""
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
        return "Invalid operation", 400  # Returns 400 Bad Request for invalid ops
    
    return str(result)

# Run the application if this file is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)