import gradio as gr
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
import requests
from io import BytesIO

# Load pre-trained model and feature extractor from Hugging Face
model_name = "microsoft/resnet-50"  # Example model; replace with your specific model if needed
extractor = AutoFeatureExtractor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)


def predict(image):
    # Preprocess the image and make predictions
    inputs = extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()

    # Convert to class label (You might need to map indices to labels)
    # This example assumes a mapping file is not needed; adjust accordingly
    class_labels = model.config.id2label
    predicted_label = class_labels[predicted_class_idx]

    return predicted_label


# Define Gradio interface
interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Upload an image of food"),
    outputs=gr.Textbox(label="Predicted Food Category"),
    title="Food Category Prediction",
    description="Upload an image of food to get the predicted food category using a pre-trained model."
)

if __name__ == "__main__":
    interface.launch()
