import numpy as np
import pandas as pd
import pickle
import sklearn

from flask import Flask, request, jsonify, render_template
from waitress import serve

app = Flask(__name__)

model = pickle.load(open('FootballApp\\data\\model.pkl', 'rb'))
label = pickle.load(open('FootballApp\\data\\labelBin.pkl', 'rb'))
x2020 = pd.read_csv("FootballApp\\data\\y2020x.csv", encoding = "UTF-8")
features = pd.read_csv("FootballApp\\data\\features.csv", encoding = "UTF-8")

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # get data
    features = dict(request.form)  

    print(features)
    
    # render with new prediction_text
    return render_template(
        './index.html',
        prediction_text='Predicted price ...')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
