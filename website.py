from flask import Flask, render_template
from flask_babel import Babel
import random

app = Flask(__name__)
babel = Babel(app)

languages = ['ca', 'en', 'es', 'fr', 'it', 'mt', 'pt', 'sv']

class Config(object):
  LANGUAGES = languages

@babel.localeselector
def get_locale():
      return 'en'

@app.route('/')
def main():
  random.shuffle(languages)
  return render_template('main.html', languages=languages)
