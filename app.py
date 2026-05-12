from flask import Flask, render_template, request
import os
from model.predict import predict_image

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def home():
    image_path = None
    prediction = None
    confidence = None

    if request.method == 'POST':

        file = request.files.get('image')

        print("File received:", file)

        if file and file.filename:

            print("Filename:", file.filename)

            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            image_path = filepath.replace("\\", "/")

            prediction, confidence = predict_image(filepath)
            confidence = round(confidence * 100, 2)

    return render_template(
        'index.html',
        image_path=image_path,
        prediction=prediction,
        confidence=confidence
    )


if __name__ == '__main__':
    app.run(debug=True)