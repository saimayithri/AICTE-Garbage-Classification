# ♻️WEEK1 SUBMISSION
# Garbage Classification using EfficientNetV2B0 (Optimized & Lightweight)

This project is an efficient, deep-learning-based solution for automatic garbage classification using **EfficientNetV2B0**, 
optimized for *lightweight* deployment and fast inference. 

---

## 📌 Key Features

- ✅ Uses EfficientNetV2B0 for balance between performance & size
- ✅ Trained on 6 classes of trash types
- ✅ Includes early stopping, learning rate scheduling, data augmentation
- ✅ Modular & clean TensorFlow/Keras implementation
- ✅ Easily convertible to TFLite for mobile/edge deployment

---

## 🛠️ Tech Stack

- TensorFlow 2.x
- Keras
- EfficientNetV2B0
- Python
- Matplotlib, Seaborn (for metrics)

---

## 📁 Dataset

> Dataset: `TrashType_Image_Dataset`  
- 6 Classes  
- Automatically split into train and validation sets  
- Loaded using `tf.keras.utils.image_dataset_from_directory()`

---

## 🚀 To Run

```bash
# Install requirements
pip install tensorflow matplotlib seaborn

# Run the notebook
jupyter notebook Garbage_Classification_EffNetV2B0.ipynb
 
