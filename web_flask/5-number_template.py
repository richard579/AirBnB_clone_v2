#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """print web"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """print web"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """print C followed by the value of the text variable"""
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """print Python, followed by the value of the text variable,
    with default value of text: is cool"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """number route"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
