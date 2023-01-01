#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 15:57:26 2022

@author: mariustakei
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle #load saved model
import json 

app = FastAPI()

class model_input(BaseModel):
    # based off of colab documnet, input types
    Gender : int
    Age : int
    Height : float
    Weight : float
    Duration : float
    Heart_Rate : float
    Body_Temp : float
    
    
# load saved model

calorie_predict_model =pickle.load(open('calorie_predict_model.sav', 'rb'))


@app.post('/calorie_predict')

def calorie_pred(input_parameters : model_input):
    
    #convert input data to json 
    input_data = input_parameters.json()
    # convert json to dictionary
    input_dictionary = json.loads(input_data)    
    
    gender = input_dictionary['Gender']
    age = input_dictionary['Age']
    hgt = input_dictionary['Height']
    wgt = input_dictionary['Weight']
    dur = input_dictionary['Duration']
    hr = input_dictionary['Heart_Rate']
    bt = input_dictionary['Body_Temp']
    
    
    input_list = [gender, age, hgt, wgt, dur, hr, bt]
    
    prediction = calorie_predict_model.predict([input_list])
    
    print(prediction)