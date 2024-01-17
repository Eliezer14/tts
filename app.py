from flask import Flask
import torch
from pprint import pprint
from omegaconf import OmegaConf
from IPython.display import Audio, display

app = Flask(__name__)

pip install -r requirements.txt

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"