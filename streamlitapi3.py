import numpy as np
import streamlit as st
import joblib

# Load model
model = joblib.load(open("second water project.pkl", "rb"))

st.title('Water Quality Prediction')


# Get user input
ph = st.text_input('pH')
Hardness = st.text_input('Hardness')
Solids = st.text_input('Solids')
Chloramines = st.text_input('Chloramines')
Sulfate = st.text_input('Sulfate')
Conductivity = st.text_input('Conductivity')
Organic_carbon = st.text_input('Organic Carbon')
Trihalomethanes = st.text_input('Trihalomethanes')
Turbidity = st.text_input('Turbidity')



# Make prediction
input_data = np.array([[ph,Hardness, Solids, Chloramines, Sulfate, Conductivity,Organic_carbon,Trihalomethanes, Turbidity]])
prediction = model.predict(input_data)

# Show prediction
if st.button('prediction'):
    input_data = np.array([[ph,Hardness, Solids, Chloramines, Sulfate, Conductivity,Organic_carbon,Trihalomethanes, Turbidity]])
    prediction = model.predict(input_data)
    if prediction[0] ==1:
        st.write(f"Predicted water quality: {'portable'}")
    if prediction[0] ==0:
        st.write(f"Predicted water quality: {'not portable'}")