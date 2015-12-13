#!/usr/bin/env python

from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.debug = True
    app.reload = True
    app.run(host='0.0.0.0')
