import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved model
heart_disease_model = pickle.load(open('heart_diseases_model.sav', 'rb'))

# Page background and styling
page_bg_img = '''
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://github.com/SHAIK-RAIYAN-2022-CSE/malaria/blob/main/Images-free-abstract-minimalist-wallpaper-HD.jpg?raw=true");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0); 
    }
    .block-container {
        max-width: 700px;
        margin: 60px auto;
        padding: 30px;
        border-radius: 15px;
        background: rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(12px);
        box-shadow: 0px 6px 24px rgba(0, 0, 0, 0.8);
    }
    input {
        background-color: #f5f5f5 !important;
        color: black !important;
        border-radius: 10px;
        border: 1px solid #ccc;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #FF4500;
        color: white;
        font-size: 18px;
        padding: 12px 28px;
        border-radius: 10px;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #FF4500;
        border: 2px solid #FF4500;
    }
    h1 {
        color: #FFD700 !important;
        text-align: center;
        font-size: 36px;
        margin-bottom: 20px;
    }
    p {
        color: white;
        text-align: center;
        font-size: 18px;
        margin-bottom: 20px;
    }
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1>Heart Disease Prediction using ML</h1>", unsafe_allow_html=True)

# Collect user input
col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')
    trestbps = st.text_input('Resting Blood Pressure')
    restecg = st.text_input('Resting Electrocardiographic results')
    oldpeak = st.text_input('ST depression induced by exercise')

with col2:
    sex = st.text_input('Sex')
    chol = st.text_input('Serum Cholesterol in mg/dl')
    thalach = st.text_input('Max Heart Rate Achieved')
    slope = st.text_input('Slope of the peak ST segment')

with col3:
    cp = st.text_input('Chest Pain Type')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = True; 0 = False)')
    exang = st.text_input('Exercise Induced Angina')
    ca = st.text_input('Major Vessels Colored by Flourosopy')
    thal = st.text_input('Thal: 0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect')

# Prediction logic
heart_diagnosis = ''

if st.button('Get Heart Disease Test Result'):
    features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    prediction = heart_disease_model.predict(features)

    if prediction[0] == 1:
        heart_diagnosis = 'The person is likely to have heart disease.'
    else:
        heart_diagnosis = 'The person is unlikely to have heart disease.'

st.success(heart_diagnosis)
