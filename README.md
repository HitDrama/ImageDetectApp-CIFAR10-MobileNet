# ImageDetectApp-CIFAR10-MobileNet

A ready-to-use image recognition web application built on MobileNetV2 and trained on the CIFAR-10 dataset. Instantly predict image classes in your browser using a pretrained deep learning model.

---

## 🚀 Overview

**ImageDetectApp-CIFAR10-MobileNet** is a web-based demo that leverages MobileNetV2 for fast, accurate classification of images into 10 common categories. The app resizes uploaded images, preprocesses them for the model, and outputs both the predicted label and confidence.

---

## 🖼️ Recognized Classes

This app can classify images into the following categories:

**Classes:**  
✈️ `airplane` | 🚗 `automobile` | 🐦 `bird` | 🐱 `cat` | 🦌 `deer` | 🐶 `dog` | 🐸 `frog` | 🐴 `horse` | 🚢 `ship` | 🚚 `truck`

---

## 🏗️ Model Structure & Key Layers

- **Base Model:** [MobileNetV2](https://keras.io/api/applications/mobilenet_v2/) (pretrained on ImageNet, `include_top=False`, frozen weights)
- **Processing Pipeline:**
  - Uploaded image resized to **224x224** pixels
  - Preprocessed using `preprocess_input`
- **Top Layers:**
  - `GlobalAveragePooling2D()`
  - `Dropout` for regularization
  - `Dense(10, activation='softmax')` (outputs probabilities for each CIFAR-10 class)

---

## ⚙️ Installation & Setup

1. **Clone this repository:**
    ```bash
    git clone https://github.com/HitDrama/ImageDetectApp-CIFAR10-MobileNet.git
    cd ImageDetectApp-CIFAR10-MobileNet
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```bash
    python run.py
    ```

4. **Open your browser and visit:**
    ```
    http://127.0.0.1:5000/lession-transfer
    ```

---

## 📊 Training Curves

Below are the training and validation curves for loss and accuracy:

<div align="center">
    <img src="https://github.com/HitDrama/ImageDetectApp-CIFAR10-MobileNet/blob/main/static/training/training.png" alt="Accuracy over epochs" width="96%">
</div>

---

## 🧪 Example Results

Here are sample test images and the model’s predictions:

<div align="center">
    <img src="https://github.com/HitDrama/ImageDetectApp-CIFAR10-MobileNet/blob/main/static/training/test-plane.png" alt="Test image 1" width="40%">
    <img src="https://github.com/HitDrama/ImageDetectApp-CIFAR10-MobileNet/blob/main/static/training/bird.png" alt="Test image 2" width="40%">

</div>

---

## 💡 Project by Developer

**Dang To Nhan** 

[📧 Contact me](mailto:dangtonhan2002@gmail.com)

---
