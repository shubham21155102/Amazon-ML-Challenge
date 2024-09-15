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

# Extract features from the sample image
image_features = extract_image_features("../images/41nblnEkJ3L.jpg")
print(image_features.shape)