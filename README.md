# 🩺 Diabetes Prediction Using ML

Check your risk of diabetes by answering a few simple questions! 
🚀 [Live App](https://check-your-diabetes-risk.streamlit.app/)

## Project Overview and Significance 

Diabetes is a growing global health concern, with serious long-term health consequences if left undiagnosed or untreated. Early identification can significantly improve outcomes through timely intervention and lifestyle changes. This project leverages machine learning (ML) to **predict diabetes** using health-related indicators from a large-scale population survey (BRFSS 2015). By applying ML techniques to this real-world data, the goal is to:
- **Explore patterns** in health behaviors and demographics associated with diabetes risk.
- **Demonstrate practical use** of ML pipelines including preprocessing, feature selection, model comparison, and evaluation.
- **Increase Awareness** about diabetes risk by creating a simple that allows users to gauge their risk level by answering a few basic questions. 

## Dataset

- **Source**: [`diabetes_binary_health_indicators_BRFSS2015.csv`](https://www.cdc.gov/brfss/index.html)
- **Target**: `Diabetes_binary` (1 = Diabetes, 0 = No Diabetes)
- **Features**: 21 categorical and ordinal indicators (e.g. age, income, physical activity, mental health days)

## Project Workflow

1. **Data Preprocessing**
   - Removed duplicates and cleaned the dataset
   - Visualized the class imbalance and feature correlations

2. **Feature Selection**
   - Used the Chi-Squared test to identify the top 12 features most relevant to diabetes classification

3. **Handling Class Imbalance**
   - Applied `RandomOverSampler` to balance the dataset before training

4. **Modeling**
   - Trained and evaluated:
     - **Logistic Regression**
     - **Random Forest Classifier**
     - **XGBoost Classifier**

5. **Evaluation**
   - Compared models using precision, recall, F1-score, and accuracy
   - Plotted confusion matrix for the best model
