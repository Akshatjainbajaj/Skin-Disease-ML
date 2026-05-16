---
title: Skin Disease Detector
emoji: 🩺
colorFrom: blue
colorTo: purple
sdk: gradio
python_version: "3.10"
app_file: app.py
pinned: false
---

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange?style=for-the-badge&logo=tensorflow)
![Flask](https://img.shields.io/badge/Flask-WebApp-black?style=for-the-badge&logo=flask)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS-red?style=for-the-badge&logo=html5)
![CNN](https://img.shields.io/badge/Model-CNN-brightgreen?style=for-the-badge)
![Gradio](https://img.shields.io/badge/Gradio-UI%2FDeployment-ff69b4?style=for-the-badge&logo=gradio)

# 🩺 Skin Disease Detection using Deep Learning

A deep learning based web application that detects common skin diseases from uploaded skin images using a Convolutional Neural Network (CNN).

## 🚀 Features

- Upload skin disease images
- AI-based prediction
- Confidence score display
- Modern responsive UI
- Deep learning CNN model

## 🧠 Diseases Supported

- Acne
- Eczema
- Healthy Skin
- Tinea
- Vitiligo

> Because apparently human skin needed software updates too.

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- TensorFlow
- CNN

### Frontend
- HTML
- CSS
- Gradio

## 📁 Project Structure

```bash
SKIN_DISEASE_ML/
│
├── dataset/
│   ├── acne/
│   ├── eczema/
│   ├── healthy/
│   ├── tinea/
│   └── vitiligo/
│
├── flagged/
│   ├── img/
│   └── log.csv
│
├── model/
│   ├── evaluate.py
│   ├── predict.py
│   ├── skin_model.h5
│   └── train.py
│
├── static/
│   ├── uploads/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── test/
│   ├── acne/
│   ├── eczema/
│   ├── healthy/
│   ├── tinea/
│   └── vitiligo/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
├── .gitignore
├── .gitattributes
└── Procfile
```