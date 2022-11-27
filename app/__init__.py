#create an instance of the Flask class for web app.
from flask import Flask
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)
app.static_folder = "Static"

from app import routes