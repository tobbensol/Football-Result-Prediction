import numpy as np
import pandas as pd
import pickle

from flask import Flask, request, jsonify, render_template
from waitress import serve

import sklearn

app = Flask(__name__)

# read and prepare model 
model = pickle.load(open('model.pkl', 'rb'))
x2020 = pd.read_csv("footballApp//data//y2020x.csv", encoding = "UTF-8")

print(np.round(model.predict(x2020)))