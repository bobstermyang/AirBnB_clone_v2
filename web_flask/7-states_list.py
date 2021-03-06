#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list')
def states_html():
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
