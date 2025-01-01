import pickle
import numpy as np
import streamlit as st
import base64

# Function to set background image and text color
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        color: black;
    }}
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {{
        color: black;
    }}
    .stApp .stMarkdown p {{
        color: black;
    }}
    .stButton button {{
        background-color: #0078D7;
        color: white;
        border-radius: 5px;
        border: none;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set the background image
set_background("background.jpg")

# Load the saved model from the file
filename = 'final_model.pkl'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

# Create the Streamlit web app
st.title("Weight Prediction App")
st.write("Enter your height in feet to predict your weight.")

# Default value for height
default_height = 5.8

# Input height from the user
height_input = st.number_input("Enter the height in feet:", value=default_height, min_value=0.0)

# Predict button
if st.button('Predict'):
    # Reshape the input height to match the shape expected by the model (2D array)
    height_input_2d = np.array(height_input).reshape(1, -1)

    # Use the loaded model to make predictions
    predicted_weight = loaded_model.predict(height_input_2d)

    # Print the predicted weight
    st.write(f"Predicted weight: {predicted_weight[0, 0]} kg")
