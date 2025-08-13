
import pickle
import streamlit as st

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app layout
st.title("My ML Model App")
input_data = st.text_input("Enter input data:")
if st.button("Predict"):
    prediction = model.predict([input_data])
    st.write(f"Prediction: {prediction}")
