#Text Extraction with OCR
import easyocr

reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):
    result = reader.readtext(image_path)
    text = " ".join([res[1] for res in result])
    return text
sample_image_path = '../images/41nblnEkJ3L.jpg'
extracted_text = extract_text_from_image(sample_image_path)
print(extracted_text)


#Feature Extraction with CNN
# main.py
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# Load a pre-trained ResNet model
resnet = models.resnet50(pretrained=True)
resnet.eval()

# Image preprocessing function
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def extract_image_features(image_path):
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        features = resnet(image)
    return features.numpy().flatten()

# Example usage
image_features = extract_image_features(sample_image_path)
print(image_features.shape)

#Data Processing
import re

def extract_entity_value(extracted_text):
    # Simple regex pattern to extract "number unit" format
    pattern = r'(\d+(\.\d+)?)\s*(gram|kilogram|centimetre|inch|ounce)'
    match = re.search(pattern, extracted_text)
    if match:
        return f"{match.group(1)} {match.group(3)}"
    return ""

# Example usage
entity_value = extract_entity_value(extracted_text)
print(entity_value)

# Model Training
# main.py
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

# Prepare training data
X_image_features = [extract_image_features(f'train_images/{idx}.jpg') for idx in train_df['index']]
X_text_features = [extract_text_from_image(f'train_images/{idx}.jpg') for idx in train_df['index']]

# Encode the target variable
y = train_df['entity_value']
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split data
X_train_img, X_test_img, X_train_text, X_test_text, y_train, y_test = train_test_split(
    X_image_features, X_text_features, y_encoded, test_size=0.2, random_state=42)

# Combine image and text features in a pipeline
model_pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train the model using image features only for simplicity
model_pipeline.fit(X_train_text, y_train)

# Evaluate the model
print(f"Training accuracy: {model_pipeline.score(X_test_text, y_test)}")