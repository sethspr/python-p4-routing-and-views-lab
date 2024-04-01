#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

#http://127.0.0.1:5555/
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>', 200

#http://127.0.0.1:5555/print/hello *the last word in the path can be anything, in this case 'hello'*
@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route, 200

#http://127.0.0.1:5555/count/12
@app.route('/count/<int:number>')
def count(number):
    count = f''
    for n in range(number):
        count += f'{n}\n' # \n this is the new line character, which will put each number on a new line. 
    return count, 200
    # using join() is real world, but will not pass the tests. 
    # numbers = [str(num) for num in range(parameter)]
    # result = '/n'.join(number)
    # return result, 200

#http://127.0.0.1:5555/math/2/+/4
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2), 200
    elif operation == "-":
        return str(num1 - num2), 200
    elif operation == "*":
        return str(num1 * num2), 200
    elif operation == "div":
        return str(num1 / num2), 200
    elif operation == "%":
        return str(num1 % num2), 200
    else:
        return f'invalid operator: {operation}', 404
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
