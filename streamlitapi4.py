import numpy as np
import streamlit as st
import joblib

# Load model
model = joblib.load("second_water_project.joblib")  # Ensure the model file is saved as .joblib

st.title('Water Quality Prediction')

# Get user input
ph = st.text_input('pH')
Hardness = st.text_input('Hardness')
Solids = st.text_input('Solids')sss
Chloramines = st.text_input('Chloramines')
Sulfate = st.text_input('Sulfate')
Conductivity = st.text_input('Conductivity')
Organic_carbon = st.text_input('Organic Carbon')
Trihalomethanes = st.text_input('Trihalomethanes')
Turbidity = st.text_input('Turbidity')

# Make prediction
if st.button('Predict'):
    try:
        # Convert inputs to float
        input_data = np.array([[float(ph), float(Hardness), float(Solids), float(Chloramines),
                                float(Sulfate), float(Conductivity), float(Organic_carbon),
                                float(Trihalomethanes), float(Turbidity)]])
        
        prediction = model.predict(input_data)
        
        # Display prediction
        if prediction[0] == 1:
            st.success("Predicted water quality: Portable")
        else:
            st.error("Predicted water quality: Not Portable")
    except ValueError:
        st.error("Please ensure all inputs are numeric!")
