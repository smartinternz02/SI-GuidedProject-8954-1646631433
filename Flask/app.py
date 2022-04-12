from copyreg import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)

with open('model.pkl','rb') as file:
    model = pickle.load(file)    

#trans=joblib.load('transform.save')


app = Flask(__name__)

@app.route('/')
def predict():
    return render_template('Manual_predict.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    values = [[float(x) for x in request.form.values()]]
    print('actual',values)
    predicted = model.predict(values)
    
    
    return render_template('Manual_predict.html', prediction_text = predicted[0])

if __name__ == '__main__':
    app.run( debug = True)
