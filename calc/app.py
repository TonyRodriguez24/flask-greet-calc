# Put your app in here.
from flask import Flask, request
from calc import operations

app = Flask(__name__)

#request.args.get()
#query parameters are a GET request
#form data is a POST

@app.route("/sub")
def sub_route():
    a = request.args.get("a", type = int)
    b = request.args.get("b", type = int)

    if a is None or b is None:
        return "Make sure entered values are correct"
    else:
        result = operations.sub(a,b)
        return f"{result}"

@app.route("/add")
def add_route():
    a = request.args.get("a", type = int)
    b = request.args.get("b", type = int)

    if a is None or b is None:
        return "Make sure entered values are correct"
    
    else:
        result = operations.add(a,b)
        return f"{result}"

@app.route("/mult")
def mult_route():
    a = request.args.get("a", type = int)
    b = request.args.get("b", type = int)

    if a is None or b is None:
        return "Make sure entered values are correct"
    else:
        result = operations.mult(a,b)
        return f"{result}"
    
@app.route("/div")
def div_route():
    a = request.args.get("a", type = int)
    b = request.args.get("b", type = int)

    if a is None or b is None:
        return "Make sure entered values are correct"
    else:
        result = operations.div(a,b)
        return f"{result}"