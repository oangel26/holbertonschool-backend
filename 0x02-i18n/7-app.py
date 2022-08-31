#!/usr/bin/env python3
"""
Infer appropriate time zone
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Optional
import pytz

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=("GET", "POST"), strict_slashes=False)
def index():
    """Function that displays info from 7-index.html"""
    return render_template('7-index.html')


class Config(object):
    """flask app config Class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('7-app.Config')


@babel.localeselector
def get_locale():
    """Function that determine the best match with
    supported languages"""
    locale = request.args.get('locale')
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    elif g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    else:
        return request.accept_languages.best_match(Config.LANGUAGES)


def get_user() -> Union[dict, None]:
    """Function that returns an user dictionary"""
    user = request.args.get('login_as', False)
    key = int(user)
    if key is not None and key in users:
        return users[key]
    else:
        return None


@app.before_request
def before_request():
    """Function that find a user if any, and set it
    as a global on flask.g.user"""
    user = get_user()
    g.user = user

@babel.timezoneselector
def get_timezone() -> Optional[str]:
    """ Determines the appropriate user timezone. """
    user_timezone = request.args.get('timezone', None)
    if not user_timezone and g.user:
        user_timezone = g.user.get('timezone')
    if user_timezone:
        try:
            return pytz.timezone(user_timezone)
        except pytz.exceptions.UnknownTimeZoneError as e:
            pass
    return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


if __name__ == '__main__':
    app.run(debug=True)
