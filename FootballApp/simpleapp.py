from flask import Flask, request, render_template
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # get data
    features = dict(request.form)  
    
    # render with new prediction_text
    return render_template(
        './index.html',
        prediction_text='Predicted price ...')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
