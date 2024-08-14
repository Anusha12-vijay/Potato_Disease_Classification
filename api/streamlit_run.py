import streamlit as st
import requests
from PIL import Image
import io

# URL of the FastAPI endpoint
API_URL = "http://localhost:8000/predict"

st.title("Potato Disease Classifier")

st.write("Upload a potato image to get a prediction.")

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Convert the image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format=image.format)
    img_bytes.seek(0)

    # Make the API request
    response = requests.post(API_URL, files={"file": img_bytes})

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        st.write("Prediction result:")
        st.write(f"Class: {result['class']}")
        st.write(f"Confidence: {result['confidence'] * 100:.2f}%")
    else:
        st.write("Error:", response.text)