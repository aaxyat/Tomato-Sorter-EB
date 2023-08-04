from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from keras.models import load_model
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Load the saved model
model = load_model('model.h5')
image_size = (128, 128)
classes = ['ripe', 'unripe']

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_image_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads', filename)
        file.save(file_path)

        image = Image.open(file_path).resize(image_size)
        image_array = np.array(image)
        image_array = image_array.astype('float32') / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(image_array)
        class_index = np.argmax(prediction[0])
        predicted_class = classes[class_index]
        if os.path.exists(file_path):
            os.remove(file_path)

        return render_template('results.html', class_name=predicted_class)

    return 'Invalid method'

if __name__ == '__main__':
    app.run()
