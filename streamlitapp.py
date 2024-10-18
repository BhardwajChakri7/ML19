import pickle
import streamlit as st

# Load the saved model
heart_disease_model = pickle.load(open('heart_diseases_model.sav', 'rb'))

# Background and styling
page_bg_img = '''
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://github.com/SHAIK-RAIYAN-2022-CSE/malaria/blob/main/Images-free-abstract-minimalist-wallpaper-HD.jpg?raw=true");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0); 
    }
    .block-container {
        max-width: 700px;
        margin: 50px auto;
        padding: 30px;
        border-radius: 20px;
        background: rgba(0, 0, 0, 0.65);
        backdrop-filter: blur(12px);
        box-shadow: 0px 8px 30px rgba(0, 0, 0, 0.7);
    }
    input {
        background-color: #fafafa !important;
        color: black !important;
        border-radius: 12px;
        border: 1px solid #bbb;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        font-size: 20px;
        padding: 12px 28px;
        border-radius: 12px;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #1E90FF;
        border: 2px solid #1E90FF;
    }
    h1 {
        color: #FFD700 !important;
        text-align: center;
        font-size: 40px;
        margin-bottom: 10px;
    }
    p {
        color: white;
        text-align: center;
        font-size: 18px;
    }
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1>💓 Heart Disease Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p>Enter your details below to check your heart health status.</p>", unsafe_allow_html=True)

# Collect user input
col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')
    trestbps = st.text_input('Resting Blood Pressure')
    restecg = st.text_input('Resting ECG Results')
    oldpeak = st.text_input('ST Depression by Exercise')

with col2:
    sex = st.text_input('Sex (0 = Female, 1 = Male)')
    chol = st.text_input('Serum Cholesterol (mg/dl)')
    thalach = st.text_input('Max Heart Rate Achieved')
    slope = st.text_input('Slope of Peak ST Segment')

with col3:
    cp = st.text_input('Chest Pain Type (0-3)')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)')
    exang = st.text_input('Exercise Induced Angina (1=True, 0=False)')
    ca = st.text_input('Major Vessels (0-4)')
    thal = st.text_input('Thal (0=Normal, 1=Fixed Defect, 2=Reversible Defect)')

# Prediction logic
heart_diagnosis = ''

if st.button('🔍 Get Prediction'):
    features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    prediction = heart_disease_model.predict(features)

    if prediction[0] == 1:
        heart_diagnosis = '⚠️ The person is likely to have heart disease.'
    else:
        heart_diagnosis = '✅ The person is unlikely to have heart disease.'

st.success(heart_diagnosis)
