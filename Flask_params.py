from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST']) # Hello World Function
def home():
    if request.method == 'GET':
        return "<h1> Hello World GET<h1>"
    elif request.method == 'POST':
        return "<h1> Hello World POST<h1>"
    else:
        return "<h1> Unknown request (Not possible to see this message)<h1>"


# Funtions suitable for "GET" request.

@app.route('/greet/<name>') # passing values through API URL.
def greet(name):
    return f"Hello {name}"

@app.route('/add/<num1>/<num2>') # By default the passing value will be strings.. (type casting another way '<int:num1>')
def add(num1, num2):
    return f"{num1} + {num2} = {int(num1) + int(num2)}"

@app.route('/url_params') # http://127.0.0.1:8000/url_params?name=bhanu&age=25 --- By this way we can pass parameters, if any parameter is missing badrequestkeyerror occurs.
def params():
    name = request.args.get('name') # or request.args['name']
    age = request.args.get('age') # or request.args['age']
    return f"name = {name}, age = {age}"


# We can specify request type by passing the methods list to route funtion. Syntax: app.route('/<url>', methods=['GET', 'POST'])
'''
Important HTTP Request types:-
------------------------------
GET = To get information
POST = To submit or creating information
PUT = To Update existing information
delete = To delete information
------------------------------
'''



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)