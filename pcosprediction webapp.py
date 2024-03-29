# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 00:02:08 2023

@author: manas
"""

import numpy as np 
import pickle
import streamlit as st

#loading the saved model 
loaded_model = pickle.load(open('D:\\pcos deployment\\trained_model.sav', 'rb'))

def pcos_pred(input_data):
    
   
    inputdataas = np.asarray(input_data)
    input_data_reshaped = inputdataas.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
        return "You don't have PCOS"
    else :
        return "You may have PCOS ,Please visit your Physician "
    
    
    
def main():
    #giving a title 
    st.title("PCOS Prediction Web App")
    
    #getting input data from the user 
    FollicleNo_R = st.text_input("Follicle number in Right Ovary")
    FollicleNo_L = st.text_input("Follicle number in Left Ovary")
    Skindarkening = st.text_input("Skin Darkening (Yes = 1 , No = 0)")
    hairgrowth = st.text_input("Hair Growth (Yes = 1 , No = 0)") 
    Weightgain= st.text_input("Weight gain  (Yes = 1 , No = 0)") 
    Cycle = st.text_input("Cycle") 
    Fastfood = st.text_input("Fast Food  (Yes = 1 , No = 0)")
    Pimples = st.text_input("Pimples (Yes = 1 , No = 0)")
    AMH = st.text_input("AMH (ng/mL)")
    Weight = st.text_input("Weight (kg)")
    BMI = st.text_input("BMI(Body Mass Index)")
    Cyclelength= st.text_input("Cycle length (days)")
    Hairloss = st.text_input("Hair Loss (Yes = 1 , No = 0)")
    Age = st.text_input("Age (Yrs)")
    Waist = st.text_input("Waist (inch)")    
    Hip = st.text_input("Hip (inch)")
    AvgFsize_L = st.text_input("Avg. Follicle size in Left Ovary  (mm)") 
    MarraigeStatus = st.text_input("Marraige Status (Yrs)")
    Endometrium = st.text_input("Endometrium (mm)")
    
    
    #code for prediction
    diagnosis = ''
    
    #creating button
    if st.button('PCOS Test Result'):
        diagnosis = pcos_pred([FollicleNo_R,FollicleNo_L,Skindarkening,hairgrowth,Weightgain,Cycle,Fastfood,Pimples,AMH,Weight,BMI,Cyclelength,Hairloss,Age,Waist,Hip,AvgFsize_L,MarraigeStatus,Endometrium])
        
        
        
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
