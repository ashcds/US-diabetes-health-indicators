import streamlit as st
import joblib as jl
import numpy as np
import pandas as pd

# Load the pre-trained model
model = jl.load('diabetes_model1.pkl')
st.title("Diabetes Prediction App")
st.write("This app predicts the likelihood of diabetes based on a few simple inputs about your health and lifestyle.")
st.write("Please answer the questions below for your evaluation.")

# Define a function to convert user inputs to binary
def convert_to_binary(feature):
    if feature == "Yes":
        return 1
    elif feature == "No":
        return 0
    
# Get user inputs for all features
Age_input = st.selectbox("How old you are?", list(range(1, 100))) # Convert to grouping 
Income_input = st.number_input(label="Enter your annual income ($)", min_value=0,format="%d", step=1000)# Convert to grouping 
HighBP_input = st.selectbox("Do you have high blood pressure?", ["Yes", "No"]) # Convert to binary
HighChol_input = st.selectbox("Do you have high cholesterol?", ["Yes", "No"]) # Convert to binary
BMI = st.number_input("What is your BMI?", min_value=10.0, max_value=60.0, value=25.0)
Stroke_input = st.selectbox("Have you ever had a stroke?", ["Yes", "No"]) # Convert to binary
HeartDiseaseorAttack_input = st.selectbox("Do you have any history of heart disease or heart attack?", ["Yes", "No"]) # Convert to binary
HvyAlcoholConsump_input = st.selectbox("Do you consume over 14 drinks/week (male) or over 7 drinks/week (female)?", ["Yes", "No"]) # Convert to binary
GenHlth = st.slider("How would you rate you health overall? (1 = Excellent, 5 = Poor)", 1, 5, 3)
MentHlth = st.slider("Thinking about your mental health, including stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?", 0, 30, 0)
PhysHlth = st.slider("Thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?", 0, 30, 0)
DiffWalk_input = st.selectbox("Do you experience difficulty walking?", ["Yes", "No"]) # Convert to binary


# Convert categorical inputs to binary
HighBP = convert_to_binary(HighBP_input)
HighChol = convert_to_binary(HighChol_input)
Stroke = convert_to_binary(Stroke_input)
HeartDiseaseorAttack = convert_to_binary(HeartDiseaseorAttack_input)
HvyAlcoholConsump = convert_to_binary(HvyAlcoholConsump_input)
DiffWalk = convert_to_binary(DiffWalk_input)

# Convert Age and Income to categorical
if Age_input < 25:
    Age = 1
elif Age_input < 30:
    Age = 2
elif Age_input < 35:
    Age = 3
elif Age_input < 40:
    Age = 4
elif Age_input < 45:
    Age = 5
elif Age_input < 50:
    Age = 6
elif Age_input < 55:
    Age = 7
elif Age_input < 60:
    Age = 8
elif Age_input < 65:
    Age = 9
elif Age_input < 70:
    Age = 10
elif Age_input < 75:
    Age = 11
else:
    Age = 12

if Income_input < 10000:
    Income = 1
elif Income_input < 15000:
    Income = 2
elif Income_input < 20000:
    Income = 3
elif Income_input < 25000:
    Income = 4
elif Income_input < 35000:
    Income = 5
elif Income_input < 50000:
    Income = 6
elif Income_input < 75000:
    Income = 7
else:
    Income = 8

# Create input array
features = pd.DataFrame([[
    HighBP, HighChol, BMI, Stroke,
    HeartDiseaseorAttack, HvyAlcoholConsump,
    GenHlth, MentHlth, PhysHlth, DiffWalk,
    Age, Income
]], columns=[
    'HighBP', 'HighChol', 'BMI', 'Stroke',
    'HeartDiseaseorAttack', 'HvyAlcoholConsump',
    'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk',
    'Age', 'Income'
])

st.write("Input Data:")
st.write(features)
st.write("Shape:", features.shape)
st.write("Missing values:", features.isnull().sum())


# Make prediction
if st.button("Predict Diabetes Risk"):
    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1] * 100
    if prediction[0] == 1:
        st.error(f"⚠️ High risk of diabetes ({probability:.1f}%)")
    else:
        st.success(f"✅ Low risk of diabetes ({probability:.1f}%)")