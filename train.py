import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator

# Step 1: Dataset Preparation
data_directory = 'data'
classes = ['ripe', 'unripe']
image_size = (128, 128)
images = []
labels = []

for class_name in classes:
    class_directory = os.path.join(data_directory, class_name)
    for image_name in os.listdir(class_directory):
        image_path = os.path.join(class_directory, image_name)
        image = Image.open(image_path).resize(image_size)
        
        # Remove alpha channel if exists
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        
        images.append(np.array(image))
        labels.append(class_name)

# Step 2: Data Preprocessing
images = np.asarray(images)
labels = np.asarray(labels)

# Normalize pixel values to range 0-1
images = images.astype('float32') / 255.0

# Convert labels to integers
label_mapping = {class_name: index for index, class_name in enumerate(classes)}
labels = np.array([label_mapping[label] for label in labels])

# Split the dataset into training and testing sets
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

# Step 3: Model Creation and Training
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(image_size[0], image_size[1], 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(len(classes), activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Augment the training data with transformations to improve model generalization
datagen = ImageDataGenerator(rotation_range=20, width_shift_range=0.2, height_shift_range=0.2, horizontal_flip=True)
datagen.fit(train_images)

model.fit(datagen.flow(train_images, train_labels, batch_size=32), epochs=10)

# Step 4: Model Evaluation
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy}")

model.save('model.h5')

