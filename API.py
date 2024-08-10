# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:22:33 2024

@author: Malipeddi Likhita
"""

import pickle
import json
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

class model_input(BaseModel):
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
 
@app.post('/diabetes_prediction')

def diabetes_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['Pregnancies']
    gluc = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insuin']
    bmi = input_dictionary['PBMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    input_list = [preg,gluc,bp,skin,insulin,bmi,dpf,age]
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0 :
        return 'The person is  not diabetic'
    else:
        return 'The person is diabetic'
    
    