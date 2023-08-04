from keras.models import load_model

# Load the saved model
model = load_model('model.h5')

from PIL import Image
import numpy as np

# Load and resize the new image
image_path = 'tomato.jpg'  # Replace with the path to your new image
image_size = (128, 128)
image = Image.open(image_path).resize(image_size)

# Convert the image to a NumPy array
image_array = np.array(image)

# Normalize pixel values to range 0-1
image_array = image_array.astype('float32') / 255.0

# Reshape the image to match the model's input shape
image_array = np.expand_dims(image_array, axis=0)


prediction = model.predict(image_array)
class_index = np.argmax(prediction[0])
classes = ['ripe', 'unripe']
predicted_class = classes[class_index]

print(f"The predicted class is: {predicted_class}")
