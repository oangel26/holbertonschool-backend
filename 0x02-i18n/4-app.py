#!/usr/bin/env python3
"""
Force locale with URL parameter
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=("GET", "POST"), strict_slashes=False)
def index():
    """Function that displays info from 4-index.html"""
    return render_template('4-index.html', locale=get_locale()
                           or babel.default_locale)


class Config(object):
    """flask app config Class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('4-app.Config')


@babel.localeselector
def get_locale():
    """Function that determine the best match with supported languages"""
    locale = request.args.get('locale')
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    else:
        return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run(debug=True)
