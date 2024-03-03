import cv2
import os
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

class LBPHAlgorithm:
    def __init__(self, X_train, y_train):
        self.X_train = [np.array(x) for x in X_train]  # Convert images to NumPy arrays
        self.y_train = np.array(y_train)  # Convert labels to a NumPy array
        self.model = cv2.face.LBPHFaceRecognizer_create()
        self.model.train(self.X_train, self.y_train)  # Train the model

    def predict(self, X_test):
        predictions = []
        confidences = []
        for img in X_test:
            img_array = np.array(img)  # Convert image to NumPy array
            label, confidence = self.model.predict(img_array)
            predictions.append(label)
            confidences.append(confidence)
        return predictions, confidences

# Function to load images from a folder
def load_images_from_folder(folder):
    images = []
    labels = []
    for person_id in range(1,3):#change according to number of users 
        for filename in range(1, 201):  # Assuming your image filenames range from 1 to 200
            img_path = os.path.join(folder, f"user.{person_id}.{filename}.jpg")
            try:
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # Read image as grayscale
                if img is not None:
                    images.append(img)
                    labels.append(filename)  # Using filename as label
                else:
                    print(f"Failed to read image: {img_path}")
            except Exception as e:
                print(f"Error loading image: {img_path}, Error: {e}")
        return images, labels

# Load images from the "data" folder
folder_path = "Data"  # Assuming your folder is named "data"
images, labels = load_images_from_folder(folder_path)

# Function to preprocess images
def preprocess_images(images, size=(100, 100)):
    processed_images = []
    for img in images:
        resized_img = cv2.resize(img, size)  # Resize image
        processed_images.append(resized_img)
    return processed_images

# Preprocess images
processed_images = preprocess_images(images)

# Now you have the preprocessed images and their corresponding labels ready for further processing or training.

# Now you can use X_train, X_test as features and y_train, y_test as labels for training and testing your model.

# Step 1: Split Data
X = processed_images  # Features (images)
y = labels  # Labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Train LBPH Algorithm
lbph = LBPHAlgorithm(X_train, y_train)

# Step 3: Set Confidence Threshold Range
confidence_thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# Step 4-6: Test with Various Thresholds and Analyze Performance
best_threshold = None
best_metric = 0

for threshold in confidence_thresholds:
    y_pred, confidences = lbph.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=1)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=1)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=1)
    
    print(f"Threshold: {threshold}, Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1: {f1}")
    
    # Update best threshold based on desired metric (e.g., F1 score)
    if f1 > best_metric:
        best_metric = f1
        best_threshold = threshold

print(f"Best Threshold: {best_threshold}, Best F1 Score: {best_metric}")

# Step 7: Validation (if needed)