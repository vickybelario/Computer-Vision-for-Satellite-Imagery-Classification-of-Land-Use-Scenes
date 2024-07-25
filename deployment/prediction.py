import streamlit as st  #mengimpor Streamlit
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import numpy as np

def import_and_predict(image_data, model):
    target_size = (256, 256)  # Set the target size to match the model's input shape
    image = load_img(image_data, target_size=target_size)  # Load and resize the image
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, 0)  # Create a batch

    # Normalize the image
    img_array = img_array / 255.0

    # Make prediction
    predictions = model.predict(img_array)

    # Get the class with the highest probability
    predicted_class = np.argmax(predictions)

    # Define the Class Names
    class_names = ['agricultural', 'airplane', 'baseballdiamond', 'beach', 'buildings',
                   'chaparral', 'denseresidential', 'forest', 'freeway', 'golfcourse',
                   'harbor', 'intersection', 'mediumresidential', 'mobilehomepark', 'overpass',
                   'parkinglot', 'river', 'runway', 'sparseresidential', 'storagetanks', 'tenniscourt']

    result = f"Prediction: {class_names[predicted_class]}"
    return result

def run():
    st.header('Model Prediction')
    st.write('Upload an image for prediction')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Perform inference if file is uploaded
        image = load_img(uploaded_file, target_size=(256, 256))
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        model = load_model('model_final.keras')  # Load  trained model
        prediction = import_and_predict(uploaded_file, model)

        st.write(prediction)