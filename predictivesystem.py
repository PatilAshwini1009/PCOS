# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 
import pickle 
#loading the saved model 
loaded_model = pickle.load(open('D:\\pcos deployment\\trained_model.sav', 'rb'))

input_data = (6,5,1,0,1,4,0,1,3.05,55,16.02307323,9,1,23,30,44,13,0,7.5)
inputdataas = np.asarray(input_data)
input_data_reshaped = inputdataas.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
    print("You don't have PCOS")
else :
    print("You may have PCOS ,Please visit your Physician ")
