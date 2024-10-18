import pickle
import streamlit as st

# Loading the saved models
Typhoid_project = pickle.load(open('Typhoid_model.sav', 'rb'))

# Custom CSS for styling
st.markdown("""
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
""", unsafe_allow_html=True)

# Page title
st.title('Typhoid Disease Prediction using ML')

# Getting the input data from the user
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Fever = st.text_input('Fever')
    
with col2:
    Cough = st.text_input('Cough')

with col3:
    Abdominal_Pain = st.text_input('Abdominal Pain')
    
with col4:
    Nausea = st.text_input('Nausea')
    
with col5:
    Vomiting = st.text_input('Vomiting')

with col1:
    Body_Temperature_High = st.text_input('Body Temperature High')
    
with col2:
    Diarrhea = st.text_input('Diarrhea')

with col3:
    Loss_of_Appetite = st.text_input('Loss of Appetite')

with col4:
    Weakness = st.text_input('Weakness')

# Code for Prediction
Typhoid_diagnosis = ''

# Creating a button for Prediction
if st.button('Typhoid Disease Test Button'):
    try:
        # Make sure to convert input to the correct data type if necessary
        inputs = [
            float(Fever),
            float(Cough),
            float(Abdominal_Pain),
            float(Nausea),
            float(Vomiting),
            float(Body_Temperature_High),
            float(Diarrhea),
            float(Loss_of_Appetite),
            float(Weakness)
        ]
        Typhoid_disease_prediction = Typhoid_project.predict([inputs])
    except ValueError as e:
        st.error(f"Prediction error: {str(e)}")
    
    if Typhoid_disease_prediction[0] == 1:
        Typhoid_diagnosis = 'The person is affected with Typhoid'
    else:
        Typhoid_diagnosis = 'The person is not affected with Typhoid'
    
st.success(Typhoid_diagnosis)
