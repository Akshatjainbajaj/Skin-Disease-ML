import gradio as gr
from model.predict import predict_image

def predict(img):
    prediction, confidence = predict_image(img)
    return f"Prediction: {prediction}\nConfidence: {confidence*100:.2f}%"

iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="filepath"),
    outputs="text",
    title="Skin Disease Detection AI",
    description="Upload a skin image to detect possible skin disease."
)

iface.launch(share=True)