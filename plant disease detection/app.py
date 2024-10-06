import streamlit as st
import tensorflow as tf
import numpy as np
import os
from PIL import Image

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the model paths
model_paths = {
    "Tomato": os.path.join(current_dir, "tomatoes.h5"),  # Update with your tomato model filename
    "Potato": os.path.join(current_dir, "potatoes.h5"),  # Update with your potato model filename
}

# Define the class names for predictions
class_names = {
    "Tomato": ['Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_healthy'],  # Update with your tomato class names
    "Potato": ['Potato_Early_blight', 'Potato_Late_blight', 'Potato_healthy'],  # Update with your potato class names
}

# Define any custom layers or functions here
# For example:
# def custom_function(x):
#     ...

# Function to make predictions
def predict(image, model_name):
    # Redefine any custom layers or functions here if needed

    loaded_model = tf.keras.models.load_model(model_paths[model_name])
    class_names_list = class_names[model_name]

    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)
    predictions = loaded_model.predict(img_array)
    predicted_class = class_names_list[np.argmax(predictions[0])]
    confidence = round(100 * np.max(predictions[0]), 2)
    return predicted_class, confidence

# Streamlit app
def main():
    st.title("Plant Leaf Disease Detection")
    st.write("Select the model and upload an image to classify the disease")

    # Model selection
    model_name = st.selectbox("Select Model", list(model_paths.keys()))

    # File uploader
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Classify"):
            prediction, confidence = predict(image, model_name)
            st.write("Prediction:", prediction)
            st.write("Confidence:", confidence, "%")

if __name__ == "__main__":
    main()
