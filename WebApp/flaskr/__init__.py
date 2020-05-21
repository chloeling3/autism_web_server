import os
import numpy as np
import flask
import joblib
from flask import Flask, render_template, request

from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

def Predictor(to_predict_list):
    #to_predict_list = np.array(to_predict_list)
    loaded_model = joblib.load('log_model.joblib')
    result = loaded_model.predict(to_predict_list)
    print(result,"RESULT")
    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list=np.zeros(19) 
        
        for i,req in enumerate(request.form):
        	to_predict_list[i]=(request.form.get(req))
        
        print(to_predict_list.shape)
        to_predict_list = np.atleast_2d(to_predict_list)
        print(to_predict_list.shape) 
        
        result = Predictor(to_predict_list)
        if int(result)==1:
            prediction='at high risk for autism.'


        else:
            prediction='at low risk for autism.'


        return render_template("result.html",prediction=prediction)
        
        
        
        
