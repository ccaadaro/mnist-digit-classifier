from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    response = requests.post('http://localhost:5000/predict', files={'file': file})
    return render_template('index.html', prediction=response.json()['prediction'])
