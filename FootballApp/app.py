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

print(model.predict(x2020))

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ''' 
    Rendering results on HTML
    '''
    # get data
    features = dict(request.form)   
    
    # expected keys
    categorical_features = ["Team", "Opponent"]
    

    # prepare for prediction
    features_df = pd.DataFrame(features, index=[0]).loc[:, numeric_features + categorical_features]
    print(features_df)
    
    # sjekk input
    if features_df.loc[0, 'LotArea'] <= 0:
        return render_template('./index.html',
                               prediction_text='LotArea must be positive')

    # predict
    prediction = model.predict(features_df)
    prediction = np.round(prediction[0])
    prediction = np.clip(prediction, 0, np.inf)

    # prepare output
    return render_template('./index.html',
                           prediction_text='Predicted price {2 - 2}'.format(prediction))

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)