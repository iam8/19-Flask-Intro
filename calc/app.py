# Ioana A Mititean
# 19.1 - Flask Greet and Calc

# NOTE: I wrote a bonus function for the route "/math/<operation>" that performs any of the 4
# math operations on 2 numbers. This wasn't requested in the exercise instructions, but the test
# file included tests for such a function.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def add_nums():
    """
    Calculate and return the result of adding two numbers.
    """

    a = request.args["a"]
    b = request.args["b"]

    return str(add(float(a), float(b)))


@app.route("/sub")
def subtract_nums():
    """
    Calculate and return the result of subtracting two numbers.
    """

    a = request.args["a"]
    b = request.args["b"]

    return str(sub(float(a), float(b)))


@app.route("/mult")
def multiply_nums():
    """
    Calculate and return the result of multiplying two numbers.
    """

    a = request.args["a"]
    b = request.args["b"]

    return str(mult(float(a), float(b)))


@app.route("/div")
def divide_nums():
    """
    Calculate and return the result of dividing two numbers.
    """

    a = request.args["a"]
    b = request.args["b"]

    return str(div(float(a), float(b)))


@app.route("/math/<operation>")
def perform_operation(operation):
    """
    Calculate and return the result of a given math operation between two numbers (add, sub, mult,
    div).
    """

    ops_dict = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div
    }

    a = request.args["a"]
    b = request.args["b"]

    result = ops_dict[operation](float(a), float(b))
    return str(result)
