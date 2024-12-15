import streamlit as st
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model

# Load the models
model1 = load_model("cat_dog_classifier.keras")  # Normal model
model2 = load_model("model_earylstopping.keras")  # Model with early stopping and dropout

def predict_image(model, img):
    img = img.resize((64, 64))  # Resize the image to the model's expected input size
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = img / 255.0  # Normalize the image

    # Make the prediction with the specific model
    prediction = model.predict(img)

    # Determine the predicted class and confidence
    if prediction[0][0] > 0.5:
        predicted_class = 'dog'
        confidence_score = prediction[0][0]
    else:
        predicted_class = 'cat'
        confidence_score = 1 - prediction[0][0]
    
    # Calculate confidence percentage
    confidence_percentage = confidence_score * 100
    return predicted_class, confidence_percentage

st.title('Cat vs Dog Classifier')
st.write("Upload an image of a cat or a dog to compare predictions from two models:")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_image:
    img = image.load_img(uploaded_image)  # Load the image

    # Show the uploaded image
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    # Make predictions using both models
    st.write("**Model 1: Normal Model**")
    prediction1, confidence1 = predict_image(model1, img)
    st.write(f"Prediction: {prediction1}")
    st.write(f"Confidence: {round(confidence1, 2)}% confident")
    
    st.write("**Model 2: Early Stopping and Dropout Model**")
    prediction2, confidence2 = predict_image(model2, img)
    st.write(f"Prediction: {prediction2}")
    st.write(f"Confidence: {round(confidence2, 2)}% confident")
