# ♻️ Smart Bin Classifier with Real-Time Animated Sorting

An AI-powered web application that classifies trash into 6 categories and displays a real-time animation of the smart bin sorting the waste — aimed at promoting automated waste segregation and eco-awareness.

---

## 🚀 Project Demo

![Smart Bin Demo](https://github.com/saimayithri/AICTE-Garbage-Classification/blob/main/Animations/cardboard.mp4)

> Upload a trash image, classify it instantly, view an eco-fact, and watch an animation of it being sorted into a smart bin!

---

## 🧠 Problem Statement

Manual waste segregation is unreliable, inconsistent, and often ignored. This leads to contamination and inefficiencies in recycling.  
**Smart Bin** solves this by automating trash classification using a lightweight AI model and simulating real-time smart bin behavior — no human intervention needed.

---

## 💡 Key Features

- ✅ Classifies trash into: `cardboard`, `glass`, `metal`, `paper`, `plastic`, and `trash`
- 📱 Runs on lightweight MobileNetV3Small model (256x256 input)
- 🌱 Displays a random eco-fact about the predicted class
- 🎬 Shows a **Blender animation** simulating physical sorting
- ⚡ Deployable using **Streamlit**
- 🧪 Uses techniques like **Label Smoothing** and **Test-Time Augmentation (TTA)** for high accuracy

---

## 📂 Folder Structure

smartbin-classifier/
├── Animations/ # Blender animation videos (MP4)
├── app.py # Streamlit frontend
├── smartbin_model.keras # Trained Keras model (MobileNetV3Small)
├── MobileNetV3Small.ipynb # Model training notebook
├── Requirements.txt # Python dependencies
└── README.md



---

## 🧠 Model Details

| Model            | Input Size | Accuracy | TTA | Label Smoothing | Notes                      |
| ---------------- | ---------- | -------- | --- | ---------------- | -------------------------- |
| MobileNetV3Small | 256x256    | 86.62%   | ✅  | ✅               | Final chosen model         |
| EfficientNetB0   | 224x224    | 84.92%   | ✅  | ❌               | Too heavy for deployment   |
| ResNet50         | 224x224    | 83.56%   | ❌  | ❌               | Good but slower inference  |
| MobileNetV2      | 224x224    | 82.10%   | ❌  | ❌               | Used as baseline           |

---

## 🛠️ Technologies Used

- **TensorFlow & Keras** — model training
- **MobileNetV3Small** — for real-time classification
- **Google Colab / Jupyter** — training notebooks
- **Streamlit** — frontend for image upload & interaction
- **Blender** — for 6-bin sorting animation
- **GitHub** — version control and project sharing

---

## ✅ Setup Instructions

1. Clone this repo:

```bash
git clone https://github.com/saimayithri/AICTE-Garbage-Classification.git
cd AICTE-Garbage-Classification/smartbin-classifier
Install dependencies:
pip install -r Requirements.txt
Run the app:
streamlit run app.py
