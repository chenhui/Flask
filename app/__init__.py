from flask import Flask
import sys , os

def config_path():
    return os.getcwd()+'/app'

def add_config_path():
    sys.path.append(config_path())

def load_config(app):
    add_config_path()
    app.config.from_object('config')

app = Flask(__name__)
load_config(app)
print(app.config.items())
from app import views