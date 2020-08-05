# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:40:01 2020

@author: nicpl
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('classifier.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)


    return render_template('index.html', prediction_text='Solar radiation Kj/m^2  {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)