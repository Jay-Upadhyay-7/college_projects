import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from PIL import Image, ImageTk

# Load the Keras model
model = load_model('trafficsign.h5')

# Preprocess the image for prediction
def preprocess_image(img):
    img = cv2.resize(img, (30, 30))
    img = np.expand_dims(img, axis=0)
    return img

# Predict the traffic sign from an image
def predict_traffic_sign(image):
    # Preprocess the image
    preprocessed_img = preprocess_image(image)

    # Make predictions
    predictions = model.predict(preprocessed_img)

    # Get the predicted class label
    predicted_class = np.argmax(predictions)
    return predicted_class

# Function to handle image upload
def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image.thumbnail((250, 250))
        photo = ImageTk.PhotoImage(image)
        img_label.config(image=photo)
        img_label.image = photo
        predicted_class = predict_traffic_sign(cv2.imread(file_path))
        result_label.config(text="Predicted Traffic Sign: " + classes[predicted_class])

# Assigning Labels
classes = {0:'Speed limit (20km/h)', 1:'Speed limit (30km/h)', 2:'Speed limit (50km/h)', 3:'Speed limit (60km/h)',
           4:'Speed limit (70km/h)', 5:'Speed limit (80km/h)', 6:'End of speed limit (80km/h)', 7:'Speed limit (100km/h)',
           8:'Speed limit (120km/h)', 9:'No passing', 10:'No passing veh over 3.5 tons', 11:'Right-of-way at intersection',
           12:'Priority road', 13:'Yield', 14:'Stop', 15:'No vehicles', 16:'Veh > 3.5 tons prohibited', 17:'No entry',
           18:'General caution', 19:'Dangerous curve left', 20:'Dangerous curve right', 21:'Double curve',
           22:'Bumpy road', 23:'Slippery road', 24:'Road narrows on the right', 25:'Road work', 26:'Traffic signals',
           27:'Pedestrians', 28:'Children crossing', 29:'Bicycles crossing', 30:'Beware of ice/snow', 31:'Wild animals crossing',
           32:'End speed + passing limits', 33:'Turn right ahead', 34:'Turn left ahead', 35:'Ahead only',
           36:'Go straight or right', 37:'Go straight or left', 38:'Keep right', 39:'Keep left', 40:'Roundabout mandatory',
           41:'End of no passing', 42:'End no passing veh > 3.5 tons'}

# Create the main window
root = tk.Tk()
root.title("Traffic Sign Detection")

# Set window size and center it
window_width = 400
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Add label for Traffic Sign Detection
title_label = tk.Label(root, text="Traffic Sign Detection", font=("Helvetica", 16))
title_label.pack(pady=10)

# Add a button to upload image
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

# Label to display uploaded image
img_label = tk.Label(root)
img_label.pack(pady=10)

# Label to display prediction
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
