from flask import Flask, render_template,request,jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import customdata, predictpipeline


app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('home.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=customdata(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),    
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=int(request.form.get('reading_score')),
            writing_score=int(request.form.get('writing_score'))
        )
        prediction=data.get_data_as_dataframe()
        predictor=predictpipeline()
        result=predictor.predict(prediction)
        return render_template('home.html',result=result[0])

if __name__ == '__main__':
    app.run(host="0.0.0.0")
