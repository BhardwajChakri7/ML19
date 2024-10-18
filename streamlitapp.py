import pickle
import streamlit as st

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

# Setting default values and ranges for inputs
with col1:
    age = st.number_input('Age', min_value=1, max_value=120, value=30)
    
with col2:
    sex = st.selectbox('Sex', options=['0 = Female', '1 = Male'], index=1)
    
with col3:
    cp = st.selectbox('Chest Pain types', options=['0 = Typical Angina', '1 = Atypical Angina', '2 = Non-Anginal Pain', '3 = Asymptomatic'], index=0)
    
with col1:
    trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=200, value=120)
    
with col2:
    chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0, max_value=600, value=200)
    
with col3:
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=['0 = False', '1 = True'], index=0)
    
with col1:
    restecg = st.selectbox('Resting Electrocardiographic results', options=['0 = Normal', '1 = Having ST-T wave abnormality', '2 = Showing probable or definite left ventricular hypertrophy'], index=0)
    
with col2:
    thalach = st.number_input('Maximum Heart Rate achieved', min_value=60, max_value=220, value=150)
    
with col3:
    exang = st.selectbox('Exercise Induced Angina', options=['0 = No', '1 = Yes'], index=0)
    
with col1:
    oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0, max_value=10.0, value=1.0)
    
with col2:
    slope = st.selectbox('Slope of the peak exercise ST segment', options=['0 = Upsloping', '1 = Flat', '2 = Downsloping'], index=1)
    
with col3:
    ca = st.number_input('Major vessels colored by flourosopy', min_value=0, max_value=4, value=0)
    
with col1:
    thal = st.selectbox('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect', options=['0 = Normal', '1 = Fixed defect', '2 = Reversible defect'], index=0)

# code for Prediction
heart_diagnosis = ''

# creating a button for Prediction
if st.button('Heart Disease Test Result'):
    heart_prediction = heart_disease_model.predict([[age, int(sex.split(' ')[0]), int(cp.split(' ')[0]), trestbps, chol, int(fbs.split(' ')[0]), int(restecg.split(' ')[0]), thalach, int(exang.split(' ')[0]), oldpeak, int(slope.split(' ')[0]), ca, int(thal.split(' ')[0])]])
    
    if (heart_prediction[0] == 1):
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'
    
st.success(heart_diagnosis)
