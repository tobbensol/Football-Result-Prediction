import numpy as np
import pandas as pd
import pickle
import sklearn

from flask import Flask, request, jsonify, render_template
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # get data
    choices = dict(request.form)  

    #imports extra data
    features = pd.read_csv("data\\features.csv", encoding = "UTF-8")
    model = pickle.load(open('data\\model.pkl', 'rb'))
    label = pickle.load(open('data\\labelBin.pkl', 'rb'))
    
    #makes a bare bones dataframe that contains the data we got from choices so that we can add data to it
    X = pd.DataFrame(
        [[choices["Home"], choices["Away"], 1],
        [choices["Away"], choices["Home"], 0]]
        ,columns=["Team", "Opponent", "Venue"])

    #i merge the extra 2019 features on both team and opponent 
    X = pd.merge(X, features, how = 'left', on=["Team"])
    features = features.rename(columns={"Team": "Opponent"})
    X = pd.merge(X, features, how = 'left', on=["Opponent"])

    #adds the labelbinalized Team and Opponent to the dataframe and removes the team and opponent collumn
    X = pd.concat([X, pd.DataFrame(label.transform(X["Team"]))], axis=1)
    X = pd.concat([X, pd.DataFrame(label.transform(X["Opponent"]))], axis=1)
    X = X.drop(["Team", "Opponent"], axis = 1).fillna(0)

    # makes the prediction
    prediction = model.predict(X)

    # render with new prediction_text
    return render_template(
        './index.html',
        prediction_text= f'Predicted score: {choices["Home"]} {round(prediction[0])} - {round(prediction[1])} {choices["Away"]}')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
