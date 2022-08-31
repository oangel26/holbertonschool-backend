#!/usr/bin/env python3
"""
Parametrize templates
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=("GET", "POST"), strict_slashes=False)
def index():
    """Function that displays info from 3-index.html"""
    return render_template('3-index.html')


class Config(object):
    """flask app config Class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('3-app.Config')


@babel.localeselector
def get_locale():
    """Function that determine the best match with supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
