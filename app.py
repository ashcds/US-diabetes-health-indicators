import streamlit as st
import joblib as jl
import numpy as np

# Load the pre-trained model
# model = jl.load('diabetes_model.pkl')

st.title("Diabetes Prediction App")
st.write("This app predicts the likelihood of diabetes based on a few simple inputs about your health and lifestyle.")

# Get user inputs
age = st.number_input("Age", min_value=1, max_value=120, value=30)