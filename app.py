import streamlit as st
import joblib as jl
import numpy as np

# Load the pre-trained model
model = jl.load('diabetes_model.pkl')
st.title("Diabetes Prediction App")
st.write("This app predicts the likelihood of diabetes based on a few simple inputs about your health and lifestyle.")
st.write("Please answer the questions below for your evaluation.")

# Get user inputs for all features
HighBP = st.selectbox("Do you have high blood pressure?", [0, 1])
HighChol = st.selectbox("Do you have high cholesterol?", [0, 1])
BMI = st.number_input("What is your BMI?", min_value=10.0, max_value=60.0, value=25.0)
Stroke = st.selectbox("Have you ever had a stroke?", [0, 1])
HeartDiseaseorAttack = st.selectbox("Heart disease or heart attack history?", [0, 1])
HvyAlcoholConsump = st.selectbox("Heavy alcohol consumption (men >14 drinks/week, women >7)?", [0, 1])
GenHlth = st.slider("General health (1 = Excellent, 5 = Poor)", 1, 5, 3)
MentHlth = st.slider("Number of days mental health was not good (past 30 days)", 0, 30, 0)
PhysHlth = st.slider("Number of days physical health was not good (past 30 days)", 0, 30, 0)
DiffWalk = st.selectbox("Do you have difficulty walking?", [0, 1])
Age = st.selectbox("Age group", list(range(1, 14)))  # Assuming age was binned into categories 1–13
Income = st.selectbox("Income level", list(range(1, 9)))  # Assuming 1 = lowest, 8 = highest

# Create input array
features = np.array([[HighBP, HighChol, BMI, Stroke, HeartDiseaseorAttack, HvyAlcoholConsump, GenHlth, MentHlth, PhysHlth, DiffWalk, Age, Income]])

# Make prediction
if st.button("Predict Diabetes Risk"):
    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1] * 100
    if prediction[0] == 1:
        st.error(f"⚠️ High risk of diabetes ({probability:.1f}%)")
    else:
        st.success(f"✅ Low risk of diabetes ({probability:.1f}%)")