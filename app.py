from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf
import os

app = Flask(__name__)
model = tf.keras.models.load_model("model.keras")

# Optional: set class names based on your dataset folder names
class_names = ['angry', 'fear', 'happy', 'sad', 'surprise', 'excitement']

@app.route('/')
def index():
    return "Facial Expression Recognition API is running."

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    image = Image.open(file).convert('RGB').resize((48, 48))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    predictions = model.predict(image)
    predicted_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_index]
    confidence = float(np.max(predictions[0]))

    return jsonify({
        "expression": predicted_class,
        "confidence": round(confidence, 3)
    })

if __name__ == '__main__':
    app.run(debug=True)
