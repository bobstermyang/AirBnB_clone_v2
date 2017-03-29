#!/usr/bin/python3
from models import storage
from console import HBNBCommand
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def states_html(id):
    states = storage.all("State")
    if (id == None):
        return render_template('9-states.html', states=states, id='all')
    else:
        for y in states.values():
            if y.id == id:
                state = y;
                return render_template('9-states.html', states=state, id='one')
        return render_template('9-states.html', states=states, id='none')

@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
