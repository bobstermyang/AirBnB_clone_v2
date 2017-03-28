#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/states', defaults={'id': ''})
@app.route('/states/', defaults={'id': ''})
@app.route('/states/<id>'}
def states_html(id):
    states = storage.all("State")
    return render_template('9-states.html', states=states, id=id)

@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
