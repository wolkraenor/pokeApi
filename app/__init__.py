from flask import Flask
from app.settings import DEBUG

app = Flask(__name__)
app.debug = DEBUG

from . import urls
