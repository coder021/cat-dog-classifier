import streamlit as st
from tensorflow.keras.preprocessing import image  # Make sure to import from tensorflow.keras
import numpy as np
from tensorflow.keras.models import load_model  # Correct the import here
model = load_model("cat_dog_classifier.keras")  # Use the load_model function to load the model

def predict_image(img):
    img = img.resize((64, 64))
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    prediction = model.predict(img)
    return 'dog' if prediction[0][0] > 0.5 else 'cat'

st.title('Cat vs Dog Classifier')
st.write("Upload an image of a cat or a dog to predict")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_image:
    img = image.load_img(uploaded_image)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    st.write("")
    prediction = predict_image(img)
    st.write(f"Prediction: {prediction}")
