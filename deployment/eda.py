import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
import zipfile
import requests
from io import BytesIO
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import UnidentifiedImageError

def download_and_extract_zip(url, extract_to):
    response = requests.get(url)
    with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
        zip_ref.extractall(extract_to)

def load_data():
    # Define directories
    train_dir = os.path.join(os.getcwd(), "temp/train")
    val_dir = os.path.join(os.getcwd(), "temp/validation")
    test_dir = os.path.join(os.getcwd(), "temp/test")

    # Data generators with normalization
    train_data_img = ImageDataGenerator(rescale=1./255.)
    val_data_img = ImageDataGenerator(rescale=1./255.)
    test_data_img = ImageDataGenerator(rescale=1./255.)

    train_img = train_data_img.flow_from_directory(
        train_dir,
        target_size=(256, 256),
        class_mode='categorical',
        batch_size=32,
        shuffle=False
    )

    val_img = val_data_img.flow_from_directory(
        val_dir,
        target_size=(256, 256),
        class_mode='categorical',
        batch_size=32,
        shuffle=False
    )

    test_img = test_data_img.flow_from_directory(
        test_dir,
        target_size=(256, 256),
        class_mode='categorical',
        batch_size=32,
        shuffle=False
    )

    return train_img, val_img, test_img

def collect_one_image_per_class(data_gen, class_names):
    # Function to collect one image per class
    collected_images = {}
    collected_labels = {}

    while len(collected_images) < len(class_names):
        try:
            images, labels = next(data_gen)
            for img, lbl in zip(images, labels):
                label_index = np.argmax(lbl)
                label_name = class_names[label_index]
                if label_name not in collected_images:
                    collected_images[label_name] = img
                    collected_labels[label_name] = lbl
                if len(collected_images) >= len(class_names):
                    break
        except UnidentifiedImageError:
            continue

    return collected_images, collected_labels

def plot_collected_images(collected_images, collected_labels, class_names, images_per_row=5):
    # Function to plot collected images
    num_classes = len(class_names)
    images_per_col = (num_classes + images_per_row - 1) // images_per_row

    fig, axes = plt.subplots(images_per_col, images_per_row, figsize=(images_per_row * 2, images_per_col * 2))

    for i, class_name in enumerate(class_names):
        row = i // images_per_row
        col = i % images_per_row
        ax = axes[row, col]
        ax.imshow(collected_images[class_name])
        ax.set_title(class_name)
        ax.axis('off')

    plt.tight_layout()
    st.pyplot(fig)  # Use st.pyplot() to display matplotlib figures in Streamlit

def run():
    # Main function to run EDA
    st.header('Exploratory Data Analysis')

    # URLs of the zip files
    train_zip_url = 'https://huggingface.co/spaces/vickybelario/Graded_Challenge_7/resolve/main/train.zip'
    val_zip_url = 'https://huggingface.co/spaces/vickybelario/Graded_Challenge_7/resolve/main/validation.zip'
    test_zip_url = 'https://huggingface.co/spaces/vickybelario/Graded_Challenge_7/resolve/main/test.zip'

    # Download and extract zip files
    temp_dir = os.path.join(os.getcwd(), "temp")
    os.makedirs(temp_dir, exist_ok=True)

    download_and_extract_zip(train_zip_url, os.path.join(temp_dir, "train"))
    download_and_extract_zip(val_zip_url, os.path.join(temp_dir, "validation"))
    download_and_extract_zip(test_zip_url, os.path.join(temp_dir, "test"))

    # Load data
    train_img, _, _ = load_data()

    # List of class names
    class_names = ['agricultural', 'airplane', 'baseballdiamond', 'beach', 'buildings',
                   'chaparral', 'denseresidential', 'forest', 'freeway', 'golfcourse',
                   'harbor', 'intersection', 'mediumresidential', 'mobilehomepark', 'overpass',
                   'parkinglot', 'river', 'runway', 'sparseresidential', 'storagetanks', 'tenniscourt']

    # Collect one image per class from the train_img
    collected_images, collected_labels = collect_one_image_per_class(train_img, class_names)

    # Plot the collected images
    plot_collected_images(collected_images, collected_labels, class_names, images_per_row=5)