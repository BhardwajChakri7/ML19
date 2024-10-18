import pickle
import streamlit as st
import numpy as np

# Load the saved model
heart_disease_model = pickle.load(open('heart_diseases_model.sav', 'rb'))



# Page title
st.title('Heart Disease Prediction using ML')

# Collect user input with proper numeric conversion
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', min_value=1, max_value=120, value=30)
    trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=200, value=120)
    restecg = st.number_input('Resting ECG Results (0-2)', min_value=0, max_value=2, value=0)
    oldpeak = st.number_input('ST Depression by Exercise', min_value=0.0, max_value=10.0, value=1.0, step=0.1)

with col2:
    sex = st.selectbox('Sex', [0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
    chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=600, value=200)
    thalach = st.number_input('Max Heart Rate Achieved', min_value=50, max_value=220, value=150)
    slope = st.number_input('Slope of Peak ST Segment (0-2)', min_value=0, max_value=2, value=1)

with col3:
    cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3, value=0)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    exang = st.selectbox('Exercise Induced Angina', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    ca = st.number_input('Major Vessels (0-4)', min_value=0, max_value=4, value=0)
    thal = st.number_input('Thal (0=Normal, 1=Fixed Defect, 2=Reversible Defect)', min_value=0, max_value=2, value=1)

# Prediction logic
heart_diagnosis = ''

if st.button('Heart Disease Test Result'):
    try:
        # Convert input values into a 2D numpy array
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        # Make prediction
        prediction = heart_disease_model.predict(features)

        # Display result
        if prediction[0] == 1:
            heart_diagnosis = '⚠️ The person is likely to have heart disease.'
        else:
            heart_diagnosis = '✅ The person is unlikely to have heart disease.'
    
    except ValueError as e:
        st.error(f"Input error: {e}")

st.success(heart_diagnosis)
