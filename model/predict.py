import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load model
model = load_model("model/skin_model.h5", compile=False)

# IMPORTANT: class order must match dataset folders
classes = ['acne', 'eczema', 'healthy', 'tinea', 'vitiligo']

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    confidence = float(np.max(prediction))

    return classes[class_index], confidence