import streamlit as st
import base64
import sklearn
import pandas as pd
import numpy as np
import random
from joblib import load
from sklearn.preprocessing import StandardScaler


svcmodel = load('SVC_model.joblib')
xgbmodel=load('XGB_model.joblib')
scal = load('scal_model.joblib')
models=[svcmodel,xgbmodel]
model=random.choice(models)
st.set_page_config(
    page_title="Non-alcohol fatty liver disease prediction",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This is an app to predict your risk of getting non-alcohol fatty liver disease!"
    })

def preprocess(user_input):  
    # Pre-processing user input   
    user_input = pd.DataFrame([user_input],columns=['age','male','weight','height','bmi','futime'])
    user_input=scal.fit_transform(user_input)
    
    return user_input

# front end elements of the web page 
html_temp = """ 
    <div> 
    <h2 style ="color:black;text-align:center;">Non-alcohol fatty liver disease prediction</h2> 
    </div> 
    """
      
st.markdown(html_temp, unsafe_allow_html = True) 

age=st.selectbox ("Age",range(1,100,1))
male = st.radio("Select sex: ", ('male', 'female'))
weight=st.selectbox('Weight in kg',range(1,300,1))
height=st.selectbox('Height in cm',range(1,200,1))
bmi=st.selectbox('BMI',range(1,50,1))
futime=st.selectbox ("Time to death or last follow up",range(1,10000,1))
if male=="male":
    male=1 
else: 
    male=0 
pred=model.predict(preprocess([age,male,weight,height,bmi,futime]))
print(preprocess([age,male,weight,height,bmi,futime]))

if st.button("Predict"):    
    if pred[0] == 1:
        st.error('Warning! You have high risk of dying from fatty liver!')
    else:
        st.success('You have lower risk of dying from fatty liver!')
        
st.sidebar.subheader("About")

st.sidebar.info("This web application helps you to find out whether you are at a risk of dying from fatty liver.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check whether you have a healthy liver")

st.info("Caution: This is just a prediction and not doctoral advice.") 
