# Ioana A Mititean
# 19.1 - Flask Greet and Calc

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def add_nums():
    a = request.args["a"]
    b = request.args["b"]

    return add(a, b)


@app.route("/sub")
def subtract_nums():
    a = request.args["a"]
    b = request.args["b"]

    return sub(a, b)


@app.route("/mult")
def multiply_nums():
    a = request.args["a"]
    b = request.args["b"]

    return mult(a, b)


@app.route("div")
def divide_nums():
    a = request.args["a"]
    b = request.args["b"]

    return div(a, b)
