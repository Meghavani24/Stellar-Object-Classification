import streamlit as st
import pandas as pd
import joblib

# Title of the app
st.title("Stellar Object Classifier App")
st.markdown("This app predicts whether a celestial object is a **STAR**, **GALAXY**, or **QUASAR** based on input features.")

# Load the saved model
model = joblib.load(r"C:\Users\megha\Downloads\Capstone Project\Capstone Project 2.joblib")

# Input fields for user to provide feature values
st.header("Enter Object Details:")

obj_ID = st.number_input("Object ID (obj_ID)", step=1.0)
alpha = st.number_input("Right Ascension (alpha)", step=0.01)
delta = st.number_input("Declination (delta)", step=0.01)
u = st.number_input("Ultraviolet (u)", step=0.01)
g = st.number_input("Green (g)", step=0.01)
r = st.number_input("Red (r)", step=0.01)
i = st.number_input("Near Infrared (i)", step=0.01)
z = st.number_input("Infrared (z)", step=0.01)
run_ID = st.number_input("Run ID", step=1.0)
rerun_ID = st.number_input("Rerun ID", step=1.0)
cam_col = st.number_input("Camera Column (cam_col)", step=1.0)
field_ID = st.number_input("Field ID", step=1.0)
spec_obj_ID = st.number_input("Spectroscopic Object ID (spec_obj_ID)", step=1.0)
redshift = st.number_input("Redshift", step=0.0001, format="%.5f")
plate = st.number_input("Plate ID", step=1.0)
MJD = st.number_input("Modified Julian Date (MJD)", step=1.0)
fiber_ID = st.number_input("Fiber ID", step=1.0)

# Combine inputs into a dataframe
input_df = pd.DataFrame({
    'obj_ID': [obj_ID],
    'alpha': [alpha],
    'delta': [delta],
    'u': [u],
    'g': [g],
    'r': [r],
    'i': [i],
    'z': [z],
    'run_ID': [run_ID],
    'rerun_ID': [rerun_ID],
    'cam_col': [cam_col],
    'field_ID': [field_ID],
    'spec_obj_ID': [spec_obj_ID],
    'redshift': [redshift],
    'plate': [plate],
    'MJD': [MJD],
    'fiber_ID': [fiber_ID]
})

# Generate new features if required by your model (you did this in training)
input_df['ug'] = input_df['u'] - input_df['g']
input_df['gr'] = input_df['g'] - input_df['r']
input_df['ri'] = input_df['r'] - input_df['i']
input_df['iz'] = input_df['i'] - input_df['z']

# List of features used by the model
features = ['alpha', 'delta', 'u', 'g', 'r', 'i', 'z', 'redshift', 'ug', 'gr', 'ri', 'iz']

# Predict when button is clicked
if st.button("Classify Object"):
    prediction = model.predict(input_df[features])[0]
    st.subheader("Prediction Result:")
    st.success(f"The object is predicted to be a **{prediction.upper()}**")
