#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hello_hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c_is_fun(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_is_cool(text):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>')
def n_is_num(n):
    return '{} is a number'.format(int(n))

@app.route('/number_template/<int:n>')
def n_template(n):
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
