import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
from PIL import Image
import numpy as np
import random

# Load model
model = load_model("smartbin_model.keras")

# Class names
class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# Eco facts
eco_facts = {
    'cardboard': [
        "Recycling 1 ton of cardboard saves over 9 cubic yards of landfill space!",
        "Cardboard can be recycled up to 7 times!"
    ],
    'glass': [
        "Glass is 100% recyclable and can be reused endlessly!",
        "Recycling one glass bottle saves enough energy to power a computer for 30 minutes!"
    ],
    'metal': [
        "Aluminum can be recycled forever without losing quality.",
        "Recycling a single soda can saves enough energy to run a TV for 2 hours!"
    ],
    'paper': [
        "Paper can be recycled about 5-7 times before fibers become too short.",
        "Every ton of recycled paper saves 17 trees!"
    ],
    'plastic': [
        "Only 9% of plastic ever produced has been recycled.",
        "Recycling plastic saves twice as much energy as burning it in an incinerator."
    ],
    'trash': [
        "Try to reduce general trash—most of it ends up in landfills.",
        "Composting can significantly reduce household trash."
    ]
}

# Preprocess image
def preprocess_uploaded_image(uploaded_file):
    img = Image.open(uploaded_file).convert("RGB")
    img = img.resize((256, 256))
    img_array = np.array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Streamlit UI
st.set_page_config(page_title="Smart Bin Classifier", page_icon="🗑️", layout="centered")
st.title("♻️ Smart Bin Classifier")
st.write("Upload a trash image and get an instant classification with an eco-fact!")

uploaded_file = st.file_uploader("Choose an image of trash...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", width=300)

    image = preprocess_uploaded_image(uploaded_file)
    prediction = model.predict(image)
    predicted_class = class_names[np.argmax(prediction)]

    st.markdown(f"### 🗑️ This looks like **{predicted_class.upper()}**!")

    # Fake popup: Eco fact
    show_fact = st.button("🌱 Show Eco Fact")
    if show_fact:
        st.info(random.choice(eco_facts[predicted_class]))

    # Fake popup: Sorting animation
    show_video = st.button("🎬 Watch Smart Bin Sort It")
    if show_video:
        st.video("Animations/cardboard.mp4")  # Update path later when per-class animations are ready

    st.success("✅ Sorting complete!")
