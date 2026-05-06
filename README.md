![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)

![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange?style=for-the-badge&logo=tensorflow)

![Flask](https://img.shields.io/badge/Flask-WebApp-black?style=for-the-badge&logo=flask)

![HTML](https://img.shields.io/badge/Frontend-HTML%2FCSS-red?style=for-the-badge&logo=html5)

![CNN](https://img.shields.io/badge/Model-CNN-green?style=for-the-badge)

# 🩺 Skin Disease Detection using Deep Learning

A deep learning based web application that detects common skin diseases from uploaded skin images using a Convolutional Neural Network (CNN).

Built using:
- Python
- TensorFlow / Keras
- Flask
- HTML/CSS
- CNN

---

# 🚀 Features

- Upload skin disease images through web interface
- AI-based disease prediction
- Confidence score display
- Modern responsive UI
- Flask backend integration
- Deep learning image classification model

---

# 🧠 Diseases Supported

The model currently detects:

- Acne
- Eczema
- Healthy Skin
- Tinea
- Vitiligo

Because apparently human skin needed a software update too.

---

# 🛠️ Tech Stack

## Backend
- Flask
- Python

## Machine Learning
- TensorFlow
- Keras
- NumPy

## Frontend
- HTML
- CSS

---

# 📂 Project Structure

```bash
Skin-Disease-ML/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── model/
│   ├── train.py
│   ├── predict.py
│   ├── evaluate.py
│   └── skin_model.h5
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── uploads/
│
├── dataset/
│   ├── acne/
│   ├── eczema/
│   ├── healthy/
│   ├── tinea/
│   └── vitiligo/
│
└── test/
