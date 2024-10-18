import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
heart_disease_model = pickle.load(open('heart_diseases_model.sav', 'rb'))

# page title
st.title('Heart Disease Prediction using ML')

# Adding custom styles
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://raw.githubusercontent.com/SHAIK-RAIYAN-2022-CSE/malaria/main/Images-free-abstract-minimalist-wallpaper-HD.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
    }
    .block-container {
        background: rgba(0, 0, 0, 0.5);
        padding: 20px;
        border-radius: 15px;
        max-width: 800px;
        margin: auto;
        backdrop-filter: blur(10px);
        box-shadow: 0px 6px 24px rgba(0, 0, 0, 0.8);
    }
    .stButton>button {
        background-color: #FF6347;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #FF6347;
        border: 2px solid #FF6347;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white;
        text-align: center;
    }
    input[type="text"], input[type="number"], select {
        background-color: white !important;
        color: black !important;
        border: 1px solid #FF6347;
        border-radius: 5px;
        padding: 10px;
        width: 100%;  /* Make the input box full width */
        box-sizing: border-box;  /* Include padding in width */
    }
    select {
        height: 40px; /* Adjust height for consistency */
        -webkit-appearance: none; /* Remove default styling */
        -moz-appearance: none; /* Remove default styling */
        appearance: none; /* Remove default styling */
    }
    </style>
    """, unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')
    
with col2:
    sex = st.text_input('Sex')
    
with col3:
    cp = st.text_input('Chest Pain types')
    
with col1:
    trestbps = st.text_input('Resting Blood Pressure')
    
with col2:
    chol = st.text_input('Serum Cholestoral in mg/dl')
    
with col3:
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    
with col1:
    restecg = st.text_input('Resting Electrocardiographic results')
    
with col2:
    thalach = st.text_input('Maximum Heart Rate achieved')
    
with col3:
    exang = st.text_input('Exercise Induced Angina')
    
with col1:
    oldpeak = st.text_input('ST depression induced by exercise')
    
with col2:
    slope = st.text_input('Slope of the peak exercise ST segment')
    
with col3:
    ca = st.text_input('Major vessels colored by flourosopy')
    
with col1:
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
# code for Prediction
heart_diagnosis = ''

# creating a button for Prediction
if st.button('Heart Disease Test Result'):
    heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    if (heart_prediction[0] == 1):
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'
    
st.success(heart_diagnosis)
